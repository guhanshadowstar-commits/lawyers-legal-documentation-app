# LegalCore

Micro-SaaS that ingests a client's batch of scanned property documents (any
mix of English / Tamil / old Tamil script), extracts structured data via a
vision LLM, sorts the batch chronologically, indexes documents by survey
number, and drafts a legal opinion for a given survey number.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the full workflow design.

## Quick start

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in GEMINI_API_KEY, DATABASE_URL, SUPABASE_URL, SUPABASE_KEY
export $(cat .env | xargs)
uvicorn app.api.main:app --reload --app-dir .
```

Storage: Postgres (via `DATABASE_URL`) for extracted data, Supabase Storage
(bucket `case-documents`, via `SUPABASE_URL`/`SUPABASE_KEY`) for the original
uploaded files. Both point at a Supabase project — create one free at
supabase.com, grab the connection string and project keys from
Project Settings, and create a Storage bucket named `case-documents`.

Open http://127.0.0.1:8000/docs for the interactive API (Swagger UI).

## API flow

1. `POST /batches` — upload a client name + the batch of files (PDF/PNG/JPG).
   Each document is OCR'd, classified, and stored.
2. `GET /batches/{batch_id}/documents` — all documents in the batch, sorted
   ascending by date.
3. `GET /batches/{batch_id}/survey/{survey_number}` — every document touching
   that survey number, in chronological order (the transaction chain).
4. `POST /batches/{batch_id}/survey/{survey_number}/opinion` — draft a legal
   opinion from that chain (placeholder template — swap in the firm's actual
   format in `backend/app/pipeline/opinion_template.py`).

## Status

MVP scaffold. Not yet built/tested end-to-end against real documents — next
step is to run a real batch through `/batches` and review extraction quality,
especially for old Tamil script.
