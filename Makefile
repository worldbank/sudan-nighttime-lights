# Makefile for Sudan Nighttime Lights Quarto Project

.PHONY: install build serve clean preview help

# Default target
help:
	@echo "Available targets:"
	@echo "  install   - Install Python dependencies"
	@echo "  build     - Build the Quarto website"
	@echo "  serve     - Serve the website locally"
	@echo "  preview   - Preview the website with live reload"
	@echo "  clean     - Clean build artifacts"
	@echo "  help      - Show this help message"

# Install dependencies
install:
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install -r requirements.txt

# Build the website
build:
	.venv/bin/quarto render

# Serve the website locally
serve:
	.venv/bin/quarto preview --port 8080

# Preview with live reload
preview:
	.venv/bin/quarto preview

# Clean build artifacts
clean:
	rm -rf _site/
	rm -rf .quarto/
	find . -name "*.html" -not -path "./_site/*" -delete
	find . -name "*_files" -type d -not -path "./_site/*" -exec rm -rf {} +

# Check Quarto installation
check:
	.venv/bin/quarto --version