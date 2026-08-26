import os

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel


class DocumentData(BaseModel):
    title: str
    summary: str
    key_topics: list[str]


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def extract_document_data(text):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"""
Extract the following information from this document:

- title
- summary
- key_topics

Document:
{text}
""",
        config={
            "response_mime_type": "application/json",
            "response_schema": DocumentData,
        },
    )

    return response.parsed