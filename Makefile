# Define paths
DATA_DOCX = data/train/Raptor_Contract.docx
EXTRACTION_SCRIPT = src/data_processing/extraction.py
GROUPING_SCRIPT = src/data_processing/grouping.py
CHUNKING_SCRIPT = src/data_processing/chunking.py
GENERATE_EMBEDDINGS_SCRIPT = src/embeddings/generate.py
PINECONE_MANAGER_SCRIPT = src/embeddings/pinecone_manager.py
RETRIEVE_SCRIPT = src/retrieval/retrieve.py
GENERATE_RESPONSE_SCRIPT = src/response_generation/generate_response.py
ARTIFACTS_DIR = artifacts
EMBEDDINGS_FILE = $(ARTIFACTS_DIR)/embeddings.json
CHUNKS_FILE = $(ARTIFACTS_DIR)/chunks.json
PINECONE_INDEX_NAME = wk11-embeddings  # Use the index name from config.py

# Default target to run all scripts
all: create_artifacts_dir extract group chunk generate_embeddings upload_embeddings retrieve generate_response

# Create artifacts directory if it doesn't exist
create_artifacts_dir:
	@mkdir -p $(ARTIFACTS_DIR)

# Extract text and metadata from DOCX
extract:
	@echo "Running extraction script..."
	PYTHONPATH=src python $(EXTRACTION_SCRIPT) --docx $(DATA_DOCX) --output $(ARTIFACTS_DIR)/output.json

# Group paragraphs into sections
group:
	@echo "Running grouping script..."
	PYTHONPATH=src python $(GROUPING_SCRIPT) --input $(ARTIFACTS_DIR)/output.json --output $(ARTIFACTS_DIR)/sections.json

# Chunk sections into manageable pieces
chunk:
	@echo "Running chunking script..."
	PYTHONPATH=src python $(CHUNKING_SCRIPT) --input $(ARTIFACTS_DIR)/sections.json --output $(CHUNKS_FILE)

# Generate embeddings
generate_embeddings:
	@echo "Generating embeddings..."
	PYTHONPATH=src python $(GENERATE_EMBEDDINGS_SCRIPT) --chunks_file $(CHUNKS_FILE) --embeddings_file $(EMBEDDINGS_FILE)

# Upload embeddings to Pinecone
upload_embeddings:
	@echo "Uploading embeddings to Pinecone..."
	PYTHONPATH=src python $(PINECONE_MANAGER_SCRIPT) --index_name $(PINECONE_INDEX_NAME) --embeddings_file $(EMBEDDINGS_FILE)

# Retrieve relevant context
retrieve:
	@echo "Running retrieval script..."
	PYTHONPATH=src python $(RETRIEVE_SCRIPT)

# Generate response
generate_response:
	@echo "Running response generation script..."
	PYTHONPATH=src python $(GENERATE_RESPONSE_SCRIPT)

# Clean up generated files
clean:
	@echo "Cleaning up..."
	rm -rf $(ARTIFACTS_DIR)

# Help target to display available commands
help:
	@echo "Makefile for running data processing and embedding scripts"
	@echo "Usage:"
	@echo "  make all             - Run all scripts in sequence"
	@echo "  make extract         - Extract text and metadata from DOCX"
	@echo "  make group           - Group paragraphs into sections"
	@echo "  make chunk           - Chunk sections into manageable pieces"
	@echo "  make generate_embeddings - Generate embeddings from chunks"
	@echo "  make upload_embeddings - Upload embeddings to Pinecone"
	@echo "  make retrieve        - Run the retrieval script"
	@echo "  make generate_response - Run the response generation script"
	@echo "  make clean           - Clean up generated files"
	@echo "  make help            - Display this help message"
