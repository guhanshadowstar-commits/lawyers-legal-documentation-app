# LegalCore — Workflow & Architecture

## Problem

A client sends a batch of 10–20 property-related documents (scans/PDFs, mixed
quality, mixed scripts: modern English, modern Tamil, old/archaic Tamil
handwriting or print). The firm needs to:

1. Read every document regardless of script/language/scan quality.
2. Identify the document type (sale deed, gift deed, partnership deed, GPA, etc.).
3. Identify the date of each document and sort the whole batch in ascending
   (chronological) order.
4. Identify the parties (from whom / to whom) on each document.
5. Identify the schedule of property (survey numbers) referenced in each
   document.
6. Given a target survey number (e.g. "2/A" out of a batch spanning "1/A"–"10/A"),
   trace every document/transaction in the batch that touches that survey
   number, in chronological order.
7. Draft a legal opinion from that chain, in a firm-specific format (format to
   be supplied later — current build stubs this stage with a placeholder
   template that is easy to swap).

## Approach

LLM-based vision pipeline: scanned pages are sent directly to a multimodal
model (Claude) which performs OCR, language identification, translation, and
structured extraction in a single pass per document. This is chosen over a
dedicated OCR engine because old/handwritten Tamil and mixed-script documents
need contextual reasoning that classical OCR (Tesseract etc.) handles poorly;
a vision LLM can read degraded scans and reason about meaning at the same time.

## Pipeline stages

```
Upload batch (N files, PDFs or images)
        |
        v
1. INGEST        -> store raw files under storage/<batch_id>/raw/, create batch record
        |
        v
2. RASTERIZE     -> convert each PDF page to an image (pages stay associated with source file)
        |
        v
3. EXTRACT       -> for each document, one vision-LLM call returns structured JSON:
                    { doc_type, doc_date, language_detected, original_script_excerpt,
                      english_translation_summary, parties: [{name, role}],
                      survey_numbers: [string], property_schedule_text,
                      consideration_amount, key_clauses, confidence_notes }
        |
        v
4. PERSIST       -> write extracted record to SQLite (documents table), linked to batch_id
        |
        v
5. SORT          -> order documents within a batch by doc_date ascending
        |
        v
6. INDEX         -> build survey_number -> [document_id...] index (a document can
                    reference multiple survey numbers)
        |
        v
7. QUERY         -> given a target survey number, fetch all linked documents in
                    chronological order = the "transaction chain"
        |
        v
8. OPINION DRAFT -> feed the ordered transaction chain to an LLM with the firm's
                    legal-opinion template -> draft opinion text (human lawyer reviews/edits)
```

## Data model (SQLite, MVP)

- `batches(id, client_name, created_at, status)`
- `documents(id, batch_id, source_filename, doc_type, doc_date, language_detected,
  parties_json, survey_numbers_json, property_schedule_text,
  consideration_amount, raw_extraction_json, created_at)`
- `survey_links(survey_number, document_id)` — derived index for fast lookup

## Why this order

- Extraction must happen before sorting/indexing (we need `doc_date` and
  `survey_numbers` to exist).
- Sorting and survey indexing are independent of each other and can happen in
  any order once extraction is done.
- Opinion drafting is the only stage that depends on a *query* (a specific
  survey number) rather than the whole batch — it's triggered on demand, not
  as part of the upload pipeline.

## Open items (need lawyer input before stage 8 is final)

- Exact legal opinion document format/template — currently stubbed in
  `backend/app/pipeline/opinion_template.py` with placeholder section headers.
- Confidence/verification UX: how should the app flag low-confidence OCR
  reads (e.g. damaged old Tamil documents) for human review before they feed
  into an opinion?
- Survey number normalization rules (e.g. "2/A" vs "2-A" vs "Survey No. 2A" —
  need a canonicalization rule so matching isn't missed by formatting
  differences).

## Stack

- Backend: Python, FastAPI, SQLite (MVP; swappable for Postgres later)
- PDF → image: PyMuPDF (`fitz`)
- Vision/extraction: Anthropic Claude API (multimodal)
- Frontend: deferred — MVP is API-first, exercised via a simple upload script
  / Swagger UI (`/docs`) until a UI is prioritized.
