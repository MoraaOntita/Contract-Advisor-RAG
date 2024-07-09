import os

# Define paths
DATA_PATH = os.path.join('data', 'train', 'Raptor_Contract.docx')
MODEL_SAVE_PATH = '/home/moraa/Documents/10_academy/week-11/notebooks/fine-tuned-model'  # Update path to the correct model location
PINECONE_INDEX_NAME = 'wk11-embeddings'

# Define model parameters
EMBEDDING_DIM = 768  # Adjust based on your SentenceTransformer model
CHUNK_SIZE = 2000
CHUNK_OVERLAP = 200

# Environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_ENVIRONMENT = os.getenv('PINECONE_ENVIRONMENT')

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Musy19@postgres:5432/wk11_db")
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")



DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@localhost:5432/mydatabase?sslmode=require")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

