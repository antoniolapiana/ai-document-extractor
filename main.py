import os
from dotenv import load_dotenv
from google import genai
from document_reader import extract_text_from_pdf


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

text = extract_text_from_pdf("example.pdf")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"Summarize this document:\n\n{text}"
)

print(response.text)