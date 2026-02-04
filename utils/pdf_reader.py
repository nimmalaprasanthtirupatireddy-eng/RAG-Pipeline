# import os
# from PyPDF2 import PdfReader
# from .logger import logger

# def read_pdf_text(pdf_path, output_dir="extracted_text"):
#     logger.info(f"Reading PDF: {pdf_path}")
#     reader = PdfReader(pdf_path)
#     text = ""

#     for i, page in enumerate(reader.pages):
#         page_text = page.extract_text() or ""
#         text += page_text + "\n"
#         logger.debug(f"Processed page {i+1}")

#     logger.info(f"Finished reading PDF ({len(reader.pages)} pages)")

#     # Save to file
#     if output_dir:
#         try:
#             os.makedirs(output_dir, exist_ok=True)
#             base_name = os.path.basename(pdf_path)
#             file_name = os.path.splitext(base_name)[0] + ".txt"
#             output_path = os.path.join(output_dir, file_name)
            
#             with open(output_path, "w", encoding="utf-8") as f:
#                 f.write(text)
#             logger.info(f"Saved extracted text to {output_path}")
#             print(f"DEBUG: Saved to {output_path}")
#         except Exception as e:
#             logger.error(f"Failed to save extracted text: {e}")
#             print(f"DEBUG: Failed to save: {e}")

#     return text

import os
from PyPDF2 import PdfReader
from .logger import logger

def read_pdf_text(pdf_path, output_dir="extracted_text"):
    logger.info(f"Reading PDF: {pdf_path}")
    reader = PdfReader(pdf_path)
    text = ""

    for i, page in enumerate(reader.pages):
        page_text = page.extract_text() or ""
        text += page_text + "\n"
        logger.debug(f"Processed page {i+1}")

    logger.info(f"Finished reading PDF ({len(reader.pages)} pages)")

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "combined.txt")

    with open(output_path, "a", encoding="utf-8") as f:
        f.write(f"\n\n===== FILE: {os.path.basename(pdf_path)} =====\n\n")
        f.write(text)

    logger.info(f"Appended extracted text to {output_path}")
    return text
