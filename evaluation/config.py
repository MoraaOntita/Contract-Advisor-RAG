import os
from dotenv import load_dotenv

load_dotenv()

# Paths
MODEL_PATH = os.getenv('MODEL_PATH', 'model/fine-tuned-model')
PINECONE_INDEX_NAME = os.getenv('PINECONE_INDEX_NAME', 'wk11-embeddings')
PINECONE_INDEX_HOST = os.getenv('PINECONE_INDEX_HOST', 'https://wk11-embeddings-0ilef8k.svc.aped-4627-b74a.pinecone.io')

# API Keys
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Evaluation Files
CONTRACT_PATH = os.getenv('CONTRACT_PATH', '/home/moraa/Documents/10_academy/week-11/data/evaluate/Robinson Advisory.docx')
QA_PATH = os.getenv('QA_PATH', '/home/moraa/Documents/10_academy/week-11/data/evaluate/Robinson Q&A.docx')
