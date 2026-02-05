from pypdf import PdfReader

def extract_pdf_text(pdf_file):
    reader = PdfReader(pdf_file)
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        pages.append({
            "page": i + 1,
            "text": text.strip()
        })

    return pages
