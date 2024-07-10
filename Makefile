# Define the default shell
SHELL := /bin/bash

# Constants
DOCKER_CONTAINER := api_container

# Directories
SRC_DIR := src
DATA_DIR := data/train
OUTPUT_DIR := artifacts

# Scripts
EXTRACTION_SCRIPT := $(SRC_DIR)/data_processing/extraction.py
GROUPING_SCRIPT := $(SRC_DIR)/data_processing/grouping.py
CHUNKING_SCRIPT := $(SRC_DIR)/data_processing/chunking.py
EMBEDDING_SCRIPT := $(SRC_DIR)/embeddings/generate.py
RETRIEVAL_SCRIPT := $(SRC_DIR)/retrieval/retrieve.py
RESPONSE_SCRIPT := $(SRC_DIR)/response_generation/generate_response.py

# Files
DOCX_FILE := $(DATA_DIR)/Raptor_Contract.docx
OUTPUT_FILE := $(OUTPUT_DIR)/output.json
GROUPED_OUTPUT := $(OUTPUT_DIR)/grouped_output.json
CHUNKED_OUTPUT := $(OUTPUT_DIR)/chunked_output.json
EMBEDDINGS_OUTPUT := $(OUTPUT_DIR)/embeddings_output.json
RETRIEVED_OUTPUT := $(OUTPUT_DIR)/retrieved_output.json
FINAL_RESPONSE := $(OUTPUT_DIR)/final_response.json

# Targets
.PHONY: all extract group chunk embed retrieve generate_response

all: extract group chunk embed retrieve generate_response

extract:
	@echo "Running extraction script..."
	docker exec -it $(DOCKER_CONTAINER) bash -c "PYTHONPATH=src python $(EXTRACTION_SCRIPT) --docx $(DOCX_FILE) --output $(OUTPUT_FILE)"

group:
	@echo "Running grouping script..."
	docker exec -it $(DOCKER_CONTAINER) bash -c "PYTHONPATH=src python $(GROUPING_SCRIPT) --input $(OUTPUT_FILE) --output $(GROUPED_OUTPUT)"

chunk:
	@echo "Running chunking script..."
	docker exec -it $(DOCKER_CONTAINER) bash -c "PYTHONPATH=src python $(CHUNKING_SCRIPT) --input $(GROUPED_OUTPUT) --output $(CHUNKED_OUTPUT)"

embed:
	@echo "Running embedding script..."
	docker exec -it $(DOCKER_CONTAINER) bash -c "PYTHONPATH=src python $(EMBEDDING_SCRIPT) --input $(CHUNKED_OUTPUT) --output $(EMBEDDINGS_OUTPUT)"

retrieve:
	@echo "Running retrieval script..."
	docker exec -it $(DOCKER_CONTAINER) bash -c "PYTHONPATH=src python $(RETRIEVAL_SCRIPT) --input $(EMBEDDINGS_OUTPUT) --output $(RETRIEVED_OUTPUT)"

generate_response:
	@echo "Running response generation script..."
	docker exec -it $(DOCKER_CONTAINER) bash -c "PYTHONPATH=src python $(RESPONSE_SCRIPT) --input $(RETRIEVED_OUTPUT) --output $(FINAL_RESPONSE)"
