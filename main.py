from document_reader import extract_text_from_pdf
from ai_extractor import extract_document_data


pdf_path = input("Enter PDF path: ")

try:
    text = extract_text_from_pdf(pdf_path)
except FileNotFoundError:
    print("File not found.")
    exit()

data = extract_document_data(text)

print(data.title)
print(data.summary)
print(data.key_topics)