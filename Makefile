# Define paths
DATA_DOCX = data/train/Raptor\ Contract.docx
EXTRACTION_SCRIPT = src/data_processing/extraction.py
GROUPING_SCRIPT = src/data_processing/grouping.py
CHUNKING_SCRIPT = src/data_processing/chunking.py

# Default target to run all scripts
all: extract group chunk

# Extract text and metadata from DOCX
extract:
	@echo "Running extraction script..."
	PYTHONPATH=src python $(EXTRACTION_SCRIPT) --docx $(DATA_DOCX) --output data/output.json

# Group paragraphs into sections
group:
	@echo "Running grouping script..."
	PYTHONPATH=src python $(GROUPING_SCRIPT) --input data/output.json --output data/sections.json

# Chunk sections into manageable pieces
chunk:
	@echo "Running chunking script..."
	PYTHONPATH=src python $(CHUNKING_SCRIPT) --input data/sections.json --output data/chunks.json

# Clean up generated files
clean:
	@echo "Cleaning up..."
	rm -f data/output.json data/sections.json data/chunks.json

# Help target to display available commands
help:
	@echo "Makefile for running data processing scripts"
	@echo "Usage:"
	@echo "  make all      - Run all scripts in sequence"
	@echo "  make extract  - Extract text and metadata from DOCX"
	@echo "  make group    - Group paragraphs into sections"
	@echo "  make chunk    - Chunk sections into manageable pieces"
	@echo "  make clean    - Clean up generated files"
	@echo "  make help     - Display this help message"
