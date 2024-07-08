import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import Document as LangchainDocument, HumanMessage
from typing import List

# Load environment variables
load_dotenv()

# Initialize OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

def generate_response(user_prompt, relevant_contexts: List[LangchainDocument]):
    llm = ChatOpenAI(
        openai_api_key=openai_api_key,
        model_name="gpt-4",
        temperature=0.7
    )
    
    # Combine the user prompt and relevant contexts
    combined_context = "\n".join([doc.page_content for doc in relevant_contexts])
    complete_input = f"Context:\n{combined_context}\n\nUser Input:\n{user_prompt}"
    
    # Define the instruction to guide the LLM
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
    
    # Create the HumanMessage object for the prompt
    human_message = HumanMessage(content=instruction)
    
    # Generate the response using GPT-4
    response = llm([human_message])
    
    return response.content

def main():
    user_query = input("Enter your query: ")
    
    # Retrieve context using the first script
    from retrieval.retrieve import retrieve_relevant_context
    relevant_contexts = retrieve_relevant_context(user_query)
    
    # Generate a response
    response = generate_response(user_query, relevant_contexts)
    print("Generated Response:", response)

if __name__ == '__main__':
    main()
