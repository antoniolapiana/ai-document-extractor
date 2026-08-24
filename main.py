import os
from dotenv import load_dotenv
from google import genai
from document_reader import extract_text_from_pdf
from pydantic import BaseModel


class DocumentData(BaseModel):
    title: str
    summary: str
    key_topics: list[str]

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

text = extract_text_from_pdf("example.pdf")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"""
Extract the following information from this document:

- title
- summary
- key_topics

Return the result as JSON.

Document:
{text}
""",
    config={
        "response_mime_type": "application/json",
        "response_schema": DocumentData,
    },
)

data = response.parsed

print(data.title)
print(data.summary)
print(data.key_topics)