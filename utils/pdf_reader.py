from PyPDF2 import PdfReader
from .logger import logger

def read_pdf_text(pdf_path):
    logger.info(f"Reading PDF: {pdf_path}")
    reader = PdfReader(pdf_path)
    text = ""

    for i, page in enumerate(reader.pages):
        page_text = page.extract_text() or ""
        text += page_text + "\n"
        logger.debug(f"Processed page {i+1}")

    logger.info(f"Finished reading PDF ({len(reader.pages)} pages)")
    return text
