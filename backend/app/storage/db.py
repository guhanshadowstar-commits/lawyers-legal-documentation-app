import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from app.models.schemas import ExtractedDocument

DB_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "app.db"


def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_connection()
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS batches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT NOT NULL,
            created_at TEXT NOT NULL,
            status TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            batch_id INTEGER NOT NULL REFERENCES batches(id),
            source_filename TEXT NOT NULL,
            doc_type TEXT,
            doc_date TEXT,
            language_detected TEXT,
            parties_json TEXT,
            survey_numbers_json TEXT,
            property_schedule_text TEXT,
            consideration_amount TEXT,
            raw_extraction_json TEXT,
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS survey_links (
            survey_number TEXT NOT NULL,
            document_id INTEGER NOT NULL REFERENCES documents(id)
        );

        CREATE INDEX IF NOT EXISTS idx_survey_links_number ON survey_links(survey_number);
        CREATE INDEX IF NOT EXISTS idx_documents_batch ON documents(batch_id);
        """
    )
    conn.commit()
    conn.close()


def create_batch(client_name: str) -> int:
    conn = get_connection()
    cur = conn.execute(
        "INSERT INTO batches (client_name, created_at, status) VALUES (?, ?, ?)",
        (client_name, datetime.now(timezone.utc).isoformat(), "processing"),
    )
    conn.commit()
    batch_id = cur.lastrowid
    conn.close()
    return batch_id


def set_batch_status(batch_id: int, status: str) -> None:
    conn = get_connection()
    conn.execute("UPDATE batches SET status = ? WHERE id = ?", (status, batch_id))
    conn.commit()
    conn.close()


def save_document(batch_id: int, source_filename: str, extracted: ExtractedDocument) -> int:
    conn = get_connection()
    cur = conn.execute(
        """INSERT INTO documents
           (batch_id, source_filename, doc_type, doc_date, language_detected,
            parties_json, survey_numbers_json, property_schedule_text,
            consideration_amount, raw_extraction_json, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            batch_id,
            source_filename,
            extracted.doc_type,
            extracted.doc_date,
            json.dumps(extracted.language_detected),
            json.dumps([p.model_dump() for p in extracted.parties]),
            json.dumps(extracted.survey_numbers),
            extracted.property_schedule_text,
            extracted.consideration_amount,
            extracted.model_dump_json(),
            datetime.now(timezone.utc).isoformat(),
        ),
    )
    document_id = cur.lastrowid

    for survey_number in extracted.survey_numbers:
        conn.execute(
            "INSERT INTO survey_links (survey_number, document_id) VALUES (?, ?)",
            (survey_number, document_id),
        )

    conn.commit()
    conn.close()
    return document_id


def get_batch_documents_sorted(batch_id: int) -> list[sqlite3.Row]:
    """Documents in a batch, ascending by doc_date. Undated documents are placed last."""
    conn = get_connection()
    rows = conn.execute(
        """SELECT * FROM documents WHERE batch_id = ?
           ORDER BY (doc_date IS NULL), doc_date ASC""",
        (batch_id,),
    ).fetchall()
    conn.close()
    return rows


def get_documents_by_survey_number(batch_id: int, survey_number: str) -> list[sqlite3.Row]:
    """All documents in a batch linked to a survey number, ascending by doc_date."""
    conn = get_connection()
    rows = conn.execute(
        """SELECT d.* FROM documents d
           JOIN survey_links sl ON sl.document_id = d.id
           WHERE d.batch_id = ? AND sl.survey_number = ?
           ORDER BY (d.doc_date IS NULL), d.doc_date ASC""",
        (batch_id, survey_number),
    ).fetchall()
    conn.close()
    return rows
