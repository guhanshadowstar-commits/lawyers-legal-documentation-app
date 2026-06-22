import json
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse

from app.pipeline.extract import extract_document
from app.pipeline.opinion_template import draft_opinion
from app.pipeline.pdf_utils import file_to_page_images_b64
from app.storage import db

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
STORAGE_ROOT = PROJECT_ROOT / "backend" / "storage" / "raw"
FRONTEND_INDEX = PROJECT_ROOT / "frontend" / "index.html"

app = FastAPI(title="LegalCore")


@app.on_event("startup")
def on_startup() -> None:
    db.init_db()


@app.get("/")
def serve_frontend():
    return FileResponse(FRONTEND_INDEX)


@app.post("/batches")
async def create_batch(client_name: str, files: list[UploadFile] = File(...)):
    batch_id = db.create_batch(client_name)
    batch_dir = STORAGE_ROOT / str(batch_id)
    batch_dir.mkdir(parents=True, exist_ok=True)

    results = []
    for upload in files:
        dest = batch_dir / upload.filename
        dest.write_bytes(await upload.read())

        page_images = file_to_page_images_b64(dest)
        extracted = extract_document(page_images)
        document_id = db.save_document(batch_id, upload.filename, extracted)
        results.append({"document_id": document_id, "filename": upload.filename, "doc_type": extracted.doc_type})

    db.set_batch_status(batch_id, "ready")
    return {"batch_id": batch_id, "documents": results}


@app.get("/batches/{batch_id}/documents")
def list_batch_documents(batch_id: int):
    rows = db.get_batch_documents_sorted(batch_id)
    if not rows:
        raise HTTPException(status_code=404, detail="Batch not found or has no documents")
    return [
        {
            "id": row["id"],
            "source_filename": row["source_filename"],
            "doc_type": row["doc_type"],
            "doc_date": row["doc_date"],
            "parties": json.loads(row["parties_json"]),
            "survey_numbers": json.loads(row["survey_numbers_json"]),
        }
        for row in rows
    ]


@app.get("/batches/{batch_id}/survey/{survey_number}")
def get_survey_chain(batch_id: int, survey_number: str):
    rows = db.get_documents_by_survey_number(batch_id, survey_number)
    if not rows:
        raise HTTPException(status_code=404, detail="No documents found for this survey number")
    return [dict(row) for row in rows]


@app.post("/batches/{batch_id}/survey/{survey_number}/opinion")
def generate_opinion(batch_id: int, survey_number: str):
    rows = db.get_documents_by_survey_number(batch_id, survey_number)
    if not rows:
        raise HTTPException(status_code=404, detail="No documents found for this survey number")
    opinion_text = draft_opinion(survey_number, rows)
    return {"survey_number": survey_number, "opinion": opinion_text}
