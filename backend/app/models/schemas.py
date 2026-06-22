from typing import List, Optional

from pydantic import BaseModel


class Party(BaseModel):
    name: str
    role: str  # e.g. "executant/seller", "buyer", "donor", "donee", "partner"


class ExtractedDocument(BaseModel):
    doc_type: str  # e.g. "sale deed", "gift deed", "partnership deed", "GPA"
    doc_date: Optional[str]  # ISO format YYYY-MM-DD if determinable, else null
    language_detected: List[str]
    original_script_excerpt: Optional[str]
    english_translation_summary: str
    parties: List[Party]
    survey_numbers: List[str]
    property_schedule_text: Optional[str]
    consideration_amount: Optional[str]
    key_clauses: List[str]
    confidence_notes: Optional[str]


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
