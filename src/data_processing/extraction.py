from docx import Document
import re
import os

def extract_text_with_metadata(docx_path):
    try:
        doc = Document(docx_path)
        documents = []
        section_title = "No Section Title"
        paragraph_number = 0
        
        file_name = os.path.splitext(os.path.basename(docx_path))[0]

        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            if not text:
                continue

            if re.match(r'^Section \d+\.\d+', text):
                section_title = text

            metadata = {
                'file_name': file_name,
                'section_title': section_title,
                'paragraph_number': paragraph_number,
            }
            documents.append({'text': text, 'metadata': metadata})
            paragraph_number += 1

        return documents
    except Exception as e:
        print(f"Error reading {docx_path}: {e}")
        return []
