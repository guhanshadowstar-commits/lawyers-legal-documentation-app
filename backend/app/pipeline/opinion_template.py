import os
import sqlite3
from typing import Optional

import anthropic

# PLACEHOLDER: replace with the firm's actual legal opinion format once supplied.
OPINION_PROMPT_TEMPLATE = """You are a senior property lawyer drafting a Legal Opinion on Title for survey \
number {survey_number}. Below is the full chronological chain of documents in the client's file that \
reference this survey number (earliest first). Each entry is a structured extraction from the original deed.

{chain_text}

Draft a Legal Opinion with these sections:
1. Brief description of the property and survey number
2. Chronology of title (chain of transactions, devolution of title)
3. Present ownership status and parties in possession
4. Encumbrances / pending litigation noted in any document
5. Observations / discrepancies requiring clarification from the client
6. Opinion (marketable title / not marketable / marketable subject to conditions)

Write in formal legal-opinion English. Mark any conclusion that depends on a document with low \
confidence_notes as "subject to verification of original document"."""


def _format_chain(rows: list[sqlite3.Row]) -> str:
    entries = []
    for i, row in enumerate(rows, start=1):
        entries.append(
            f"--- Document {i} ---\n"
            f"Source file: {row['source_filename']}\n"
            f"Type: {row['doc_type']}\n"
            f"Date: {row['doc_date']}\n"
            f"Parties: {row['parties_json']}\n"
            f"Survey numbers: {row['survey_numbers_json']}\n"
            f"Property schedule: {row['property_schedule_text']}\n"
            f"Consideration: {row['consideration_amount']}\n"
        )
    return "\n".join(entries)


def draft_opinion(survey_number: str, chain_rows: list[sqlite3.Row], model: Optional[str] = None) -> str:
    model = model or os.environ.get("EXTRACTION_MODEL", "claude-sonnet-4-6")
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    prompt = OPINION_PROMPT_TEMPLATE.format(
        survey_number=survey_number, chain_text=_format_chain(chain_rows)
    )
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text
