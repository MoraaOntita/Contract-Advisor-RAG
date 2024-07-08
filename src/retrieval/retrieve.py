import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from pinecone import Pinecone as PineconeClient
from langchain.schema import Document

# Load environment variables
load_dotenv()

# Load the fine-tuned model from the local path
model_save_path = '/home/moraa/Documents/10_academy/week-11/notebooks/fine-tuned-model'
model = SentenceTransformer(model_save_path)

# Initialize Pinecone API key
pinecone_api_key = os.getenv('PINECONE_API_KEY')
if not pinecone_api_key:
    raise ValueError("PINECONE_API_KEY environment variable is not set.")

# Initialize Pinecone client
pc = PineconeClient(api_key=pinecone_api_key)
index_name = "wk11-embeddings"

# Initialize the index with the correct host
index_host = "https://wk11-embeddings-0ilef8k.svc.aped-4627-b74a.pinecone.io"
index = pc.Index(host=index_host)

def generate_embeddings(model, texts):
    embeddings = model.encode(texts, convert_to_numpy=True)
    return embeddings

def retrieve_relevant_context(prompt, top_k=5):
    # Generate embedding for the prompt
    prompt_embedding = generate_embeddings(model, [prompt])[0]
    
    # Query Pinecone for the most relevant documents
    results = index.query(vector=prompt_embedding.tolist(), top_k=top_k, include_metadata=True)
    
    # Extract and return the relevant documents
    relevant_documents = [
        Document(page_content=result['metadata']['text'], metadata=result['metadata'])
        for result in results['matches']
    ]
    return relevant_documents

def main():
    user_query = input("Enter your query: ")
    relevant_contexts = retrieve_relevant_context(user_query)
    for doc in relevant_contexts:
        print(f"Content: {doc.page_content}\nMetadata: {doc.metadata}\n")

if __name__ == '__main__':
    main()
