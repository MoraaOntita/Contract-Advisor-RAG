from docx import Document
import re
import os
import argparse
import json

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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--docx', required=True, help='Path to the DOCX file')
    parser.add_argument('--output', required=True, help='Path to the output JSON file')
    args = parser.parse_args()

    documents = extract_text_with_metadata(args.docx)
    with open(args.output, 'w') as f:
        json.dump(documents, f, indent=2)
    print(f"Extracted data saved to {args.output}")

if __name__ == '__main__':
    main()
