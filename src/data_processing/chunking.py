from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.config import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_sections(sections):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    
    chunks = []
    chunk_id_counter = 0  # Counter for unique chunk IDs

    for section in sections:
        try:
            split_texts = text_splitter.split_text(section['text'])
            
            for split_text in split_texts:
                chunk_metadata = {
                    'id': f"chunk_{chunk_id_counter}",  # Generate unique ID
                    'section_title': section['metadata'].get('section_title', 'No Section Title'),
                    'file_name': section['metadata'].get('file_name', 'Unknown File'),
                    'paragraph_number': section['metadata'].get('paragraph_number', 'Unknown Paragraph'),
                    'text': split_text  # Store the actual text content in metadata
                }
                chunks.append({
                    'text': split_text,
                    'metadata': chunk_metadata
                })
                chunk_id_counter += 1  # Increment the counter for the next chunk
        except Exception as e:
            print(f"Error processing section with title '{section['metadata'].get('section_title', 'Unknown')}' - {e}")

    return chunks
