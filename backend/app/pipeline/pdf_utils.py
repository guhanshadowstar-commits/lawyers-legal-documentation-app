import base64
from pathlib import Path

import fitz  # PyMuPDF


def file_to_page_images_b64(file_path: Path, dpi: int = 200) -> list[str]:
    """Convert a PDF or image file into a list of base64-encoded PNG page images."""
    suffix = file_path.suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg"}:
        return [base64.b64encode(file_path.read_bytes()).decode("utf-8")]

    images: list[str] = []
    doc = fitz.open(file_path)
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    for page in doc:
        pix = page.get_pixmap(matrix=matrix)
        images.append(base64.b64encode(pix.tobytes("png")).decode("utf-8"))
    doc.close()
    return images
