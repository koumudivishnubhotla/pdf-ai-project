import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def gemini_answer(context, question):
    prompt = f"""
You are answering strictly from the PDF content below.
If the answer is not present, say "Answer not found in the document."

PDF Content:
{context}

Question:
{question}

Answer clearly and concisely.
"""
    response = model.generate_content(prompt)
    return response.text
