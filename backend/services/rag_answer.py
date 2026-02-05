import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def generate_answer(context, question):
    model = genai.GenerativeModel(
        model_name="models/gemini-2.5-flash"
    )

    prompt = f"""
Answer the question strictly using the PDF content below.
If the answer is not found, say so clearly.

PDF CONTENT:
{context}

QUESTION:
{question}

ANSWER:
"""

    response = model.generate_content(prompt)
    return response.text