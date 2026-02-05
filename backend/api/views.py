from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from services.pdf_extract import extract_pdf_text
from services.rag_store import PDF_STORE
import uuid
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_pdf(request):
    if 'file' not in request.FILES:
        return Response({"error": "No file uploaded"}, status=400)

    pdf_file = request.FILES['file']
    pages = extract_pdf_text(pdf_file)

    doc_id = str(uuid.uuid4())

    # Store full text
    PDF_STORE[doc_id] = " ".join([p["text"] for p in pages])

    return Response({
        "doc_id": doc_id,
        "pages_extracted": len(pages)
    })


@api_view(['POST'])
def ask_pdf(request):
    doc_id = request.data.get("doc_id")
    question = request.data.get("question")

    if not doc_id or not question:
        return Response(
            {"error": "doc_id and question required"},
            status=400
        )

    if doc_id not in PDF_STORE:
        return Response(
            {"error": "Document not found"},
            status=404
        )

    # Combine PDF text
    pdf_text = " ".join(PDF_STORE[doc_id])

    # Limit context size (important!)
    pdf_text = pdf_text[:12000]

    prompt = f"""
You are an AI assistant answering questions strictly from the given PDF content.

PDF CONTENT:
{pdf_text}

QUESTION:
{question}

Answer clearly, accurately, and concisely.
If the answer is not found in the PDF, say:
"I could not find this information in the PDF."
"""

    try:
        response = model.generate_content(prompt)
        return Response({
            "answer": response.text
        })
    except Exception as e:
        return Response(
            {"error": str(e)},
            status=500
        )