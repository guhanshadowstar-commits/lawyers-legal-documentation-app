import base64

import fitz  # PyMuPDF

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg"}


def file_bytes_to_page_images_b64(filename: str, file_bytes: bytes, dpi: int = 200) -> list[str]:
    """Convert PDF or image bytes into a list of base64-encoded PNG page images."""
    suffix = "." + filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if suffix in IMAGE_SUFFIXES:
        return [base64.b64encode(file_bytes).decode("utf-8")]

    images: list[str] = []
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    for page in doc:
        pix = page.get_pixmap(matrix=matrix)
        images.append(base64.b64encode(pix.tobytes("png")).decode("utf-8"))
    doc.close()
    return images
