import base64
import json
import os

from google import genai
from google.genai import types

from app.models.schemas import ExtractedDocument

EXTRACTION_PROMPT = """You are reviewing a scanned legal property document for an Indian law firm. \
The document may be in English, Tamil, or old/archaic Tamil script (handwritten or printed), and may be \
of poor scan quality. Read all pages provided (they belong to the same document) and extract the \
following as JSON matching exactly this schema:

{
  "doc_type": string,            // e.g. "sale deed", "gift deed", "partnership deed", "GPA", "mortgage deed", "will", "lease deed"
  "doc_date": string | null,     // ISO format YYYY-MM-DD if you can determine it, else null
  "language_detected": [string], // e.g. ["Tamil"], ["English"], ["Tamil", "English"]
  "original_script_excerpt": string | null,  // a short verbatim excerpt in the original script, for human verification
  "english_translation_summary": string,     // a concise English summary of what the document says
  "parties": [{"name": string, "role": string}],  // role e.g. "seller", "buyer", "donor", "donee", "partner", "executant"
  "survey_numbers": [string],    // every survey number referenced, normalized as written (e.g. "2/A")
  "property_schedule_text": string | null,  // the property schedule / description text, translated to English
  "consideration_amount": string | null,
  "key_clauses": [string],       // notable clauses (encumbrance, possession, boundaries, conditions, etc.)
  "confidence_notes": string | null  // flag anything illegible, ambiguous, or low-confidence
}

Return ONLY the JSON object, no other text."""


DEFAULT_MODEL = os.environ.get("EXTRACTION_MODEL", "gemini-2.0-flash")


def extract_document(page_images_b64: list[str], model: str = DEFAULT_MODEL) -> ExtractedDocument:
    """Send all pages of one document to Gemini in a single call and parse the structured extraction."""
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    parts = [
        types.Part.from_bytes(data=base64.b64decode(img), mime_type="image/png")
        for img in page_images_b64
    ]
    parts.append(types.Part.from_text(text=EXTRACTION_PROMPT))

    response = client.models.generate_content(
        model=model,
        contents=parts,
        config=types.GenerateContentConfig(response_mime_type="application/json"),
    )

    data = json.loads(response.text)
    return ExtractedDocument(**data)
