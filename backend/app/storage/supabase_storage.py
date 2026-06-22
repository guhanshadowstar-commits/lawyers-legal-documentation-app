import os

from supabase import Client, create_client

BUCKET_NAME = "case-documents"


def get_client() -> Client:
    return create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])


def upload_raw_file(batch_id: int, filename: str, file_bytes: bytes) -> str:
    """Upload the original scanned document to Supabase Storage. Returns the storage path."""
    client = get_client()
    path = f"{batch_id}/{filename}"
    client.storage.from_(BUCKET_NAME).upload(
        path, file_bytes, {"content-type": "application/octet-stream", "upsert": "true"}
    )
    return path
