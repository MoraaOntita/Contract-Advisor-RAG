import pinecone
import json
import os
import argparse
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
load_dotenv()

def create_index(index_name, dimension):
    # Initialize Pinecone client
    pinecone_api_key = os.getenv('PINECONE_API_KEY')
    pc = Pinecone(api_key=pinecone_api_key)

    # Check if the index exists; if not, create it
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=dimension,  # Use the dimension of your embeddings
            metric="cosine",
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
    print(f"Index '{index_name}' is ready.")

def upload_embeddings(index_name, embeddings_file):
    # Load embeddings from file
    with open(embeddings_file, 'r') as f:
        embeddings_data = json.load(f)
    
    # Initialize Pinecone client
    pinecone_api_key = os.getenv('PINECONE_API_KEY')
    pc = Pinecone(api_key=pinecone_api_key)
    
    # Connect to the index
    index = pc.Index(index_name)
    
    # Prepare the data for Pinecone
    vectors = [(e['id'], e['embedding'], e['metadata']) for e in embeddings_data]
    
    # Upload embeddings to Pinecone
    index.upsert(vectors)
    print(f"Uploaded embeddings to Pinecone index '{index_name}'")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--index_name', required=True, help='Name of the Pinecone index')
    parser.add_argument('--embeddings_file', required=True, help='Path to the embeddings JSON file')
    args = parser.parse_args()

    # Load embeddings to determine dimension
    with open(args.embeddings_file, 'r') as f:
        embeddings_data = json.load(f)
    
    # Ensure that embeddings data is not empty
    if not embeddings_data:
        raise ValueError("No embeddings found in the file.")
    
    # Determine dimension from the first embedding
    dimension = len(embeddings_data[0]['embedding'])
    print(f"Determined embedding dimension: {dimension}")

    # Create Pinecone index
    create_index(args.index_name, dimension)

    # Upload embeddings to Pinecone
    upload_embeddings(args.index_name, args.embeddings_file)

if __name__ == '__main__':
    main()
