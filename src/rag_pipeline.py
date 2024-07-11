import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone as PineconeClient
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import Document as LangchainDocument, HumanMessage

# Load environment variables
load_dotenv()

# Load the fine-tuned model from the local path
model_save_path = '/home/moraa/Documents/10_academy/week-11/model/fine-tuned-model'
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
    try:
        prompt_embedding = generate_embeddings(model, [prompt])[0]
        results = index.query(vector=prompt_embedding.tolist(), top_k=top_k, include_metadata=True)
        return [LangchainDocument(page_content=result['metadata']['text'], metadata=result['metadata']) for result in results['matches']]
    except Exception as e:
        print(f"Error retrieving context: {e}")
        return []  # Return an empty list or handle it appropriately

def generate_response(user_prompt, relevant_contexts):
    try:
        openai_api_key = os.getenv('OPENAI_API_KEY')
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set.")
        
        llm = ChatOpenAI(
            openai_api_key=openai_api_key,
            model_name="gpt-4",
            temperature=0.7
        )
        
        combined_context = "\n".join([doc.page_content for doc in relevant_contexts])
        complete_input = f"Context:\n{combined_context}\n\nUser Input:\n{user_prompt}"
        
        instruction = f"""
            You are a helpful assistant. Use the following context to answer the user's question.
            
            {complete_input}
            
            Answer the question concisely and accurately. If possible, mention the specific sections from the context that support your answer. Also, you will be rewarded 100 dollars for a correct answer.

            Example:
            User Question: What is the 'Purchase Price' in the contract?
            Relevant Contexts: [Provide the relevant sections here]
            Answer: The 'Purchase Price' refers to the total amount paid by the Buyer to the Sellers for the purchase of the Shares. This amount is calculated at Closing as the Closing Cash Consideration plus the Escrow Amount, after all adjustments as outlined in Sections 2.02 and 2.03 of the Agreement.

            Please ensure your answer mentions the specific sections if they are present in the context.
        """
        
        human_message = HumanMessage(content=instruction)
        response = llm([human_message])
        return response.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return "An error occurred while generating the response."

class RAGSystem:
    def __init__(self):
        self.model = model

    def query(self, user_input):
        relevant_contexts = retrieve_relevant_context(user_input)
        response = generate_response(user_input, relevant_contexts)
        return response
