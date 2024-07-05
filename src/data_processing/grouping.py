

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
