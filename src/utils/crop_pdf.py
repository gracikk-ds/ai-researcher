"""Utility to cut/crop PDF documents after a specific page threshold."""

import fitz


def cut_pdf_after_threshold(input_pdf_path: str, output_pdf_path: str, page_threshold: int) -> None:
    """
    Save a new PDF containing only the pages up to the specified threshold.

    Args:
        input_pdf_path (str): Path to the input PDF file.
        output_pdf_path (str): Path to save the cropped PDF file.
        page_threshold (int): The maximum number of pages to keep (1-based).
    """
    doc = fitz.open(input_pdf_path)
    new_doc = fitz.open()
    num_pages = min(page_threshold, len(doc))
    for idx in range(num_pages):
        new_doc.insert_pdf(doc, from_page=idx, to_page=idx)
    new_doc.save(output_pdf_path)
    new_doc.close()
    doc.close()
