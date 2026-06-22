from pydantic import BaseModel


class Party(BaseModel):
    name: str
    role: str  # e.g. "executant/seller", "buyer", "donor", "donee", "partner"


class ExtractedDocument(BaseModel):
    doc_type: str  # e.g. "sale deed", "gift deed", "partnership deed", "GPA"
    doc_date: str | None  # ISO format YYYY-MM-DD if determinable, else null
    language_detected: list[str]
    original_script_excerpt: str | None
    english_translation_summary: str
    parties: list[Party]
    survey_numbers: list[str]
    property_schedule_text: str | None
    consideration_amount: str | None
    key_clauses: list[str]
    confidence_notes: str | None


class DocumentRecord(BaseModel):
    id: int
    batch_id: int
    source_filename: str
    extracted: ExtractedDocument


class Batch(BaseModel):
    id: int
    client_name: str
    created_at: str
    status: str
