import argparse
import json
import os

def group_paragraphs_into_sections(documents):
    sections = []
    current_section = {'text': '', 'metadata': {'id': 'default_id', 'section_title': 'No Section Title', 'file_name': None, 'paragraph_number': None}}

    for doc in documents:
        if doc['metadata']['section_title'] and doc['metadata']['section_title'] != "No Section Title":
            if current_section['text']:
                sections.append(current_section)
            current_section = {'text': doc['text'], 'metadata': doc['metadata']}
        else:
            if current_section['text']:
                current_section['text'] += ' ' + doc['text']
            else:
                current_section['text'] = doc['text']
    
    if current_section['text']:
        sections.append(current_section)

    return sections

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to the input JSON file')
    parser.add_argument('--output', required=True, help='Path to the output JSON file')
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        documents = json.load(f)

    sections = group_paragraphs_into_sections(documents)
    with open(args.output, 'w') as f:
        json.dump(sections, f, indent=2)
    print(f"Grouped sections saved to {args.output}")

if __name__ == '__main__':
    main()
