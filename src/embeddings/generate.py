from sentence_transformers import SentenceTransformer
import json
import os
import argparse

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Load the fine-tuned model
from config import MODEL_SAVE_PATH

# Ensure the model path is valid
if not os.path.isdir(MODEL_SAVE_PATH):
    raise FileNotFoundError(f"Model directory not found: {MODEL_SAVE_PATH}")

try:
    model = SentenceTransformer(MODEL_SAVE_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    raise

def generate_embeddings(model, chunks):
    texts = [chunk['text'] for chunk in chunks]
    embeddings = model.encode(texts, convert_to_numpy=True)
    return embeddings

def prepare_data_for_pinecone(chunks, embeddings):
    data = []
    for i, chunk in enumerate(chunks):
        metadata = chunk['metadata']
        cleaned_metadata = {k: (v if v is not None else '') for k, v in metadata.items()}
        
        data.append({
            'id': chunk['metadata']['id'],
            'embedding': embeddings[i].tolist(),  # Convert numpy array to list
            'metadata': cleaned_metadata,
            'text': chunk['text']  # Store the actual text content
        })
    return data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--chunks_file', required=True, help='Path to the chunks JSON file')
    parser.add_argument('--embeddings_file', required=True, help='Path to save the embeddings JSON file')
    args = parser.parse_args()

    # Load chunks
    with open(args.chunks_file, 'r') as f:
        chunks = json.load(f)

    # Generate embeddings
    embeddings = generate_embeddings(model, chunks)

    # Prepare data for Pinecone
    data_for_pinecone = prepare_data_for_pinecone(chunks, embeddings)

    # Save embeddings to file
    with open(args.embeddings_file, 'w') as f:
        json.dump(data_for_pinecone, f)

    print(f"Embeddings saved to {args.embeddings_file}")

if __name__ == '__main__':
    main()
