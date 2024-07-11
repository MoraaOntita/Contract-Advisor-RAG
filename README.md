# LLM_RAG_Contract-Advisor_App

## Overview

Build, Evaluate, and Improve the RAG system for Contract Q&A (chatting with a contract and asking questions about the contract).

This Chat App is a Python application that allows you to chat with contract documents. You can ask questions about the contracts, and the application will provide relevant responses based on the content of the contracts you provide. This app utilizes a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the loaded docx.

## How It Works

The application follows these steps to provide responses to your questions:

1. **PDF Loading**: The app reads multiple docx documents and extracts their text content.
2. **Text Chunking**: The extracted text is divided into smaller chunks that can be processed effectively.
3. **Language Model**: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.
4. **Similarity Matching**: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.
5. **Response Generation**: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

## Dependencies and Installation

To install, please follow these steps:

1. **Clone the repository to your local machine**:
   ```bash
   git clone https://github.com/MoraaOntita/Contract-Advisor-RAG.git

    ```
2. Install the required dependencies by running the following command:
    ```
    pip install -r requirements.txt

    ```

3. Obtain an API key from OpenAI and Huggingface and add it to the .env file in the project directory:
    ```
    OPENAI_API_KEY=your_secret_api_key
    PINECONE_API_KEY=your_secret_api_key

    ```

## Usage
Ensure that you have installed the required dependencies and added the OpenAI API or Pinecone key to the .env file.   