.PHONY: help install setup test clean lint format run

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies
	pip install -r requirements.txt

setup: ## Initial setup using setup script (recommended)
	@if [ -f setup.sh ]; then \
		chmod +x setup.sh && ./setup.sh; \
	else \
		echo "Running manual setup..."; \
		python -m venv venv; \
		. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt; \
		if [ ! -f .env ]; then cp env.example .env && echo "Created .env file. Please edit it with your API keys."; fi; \
	fi

test: ## Run tests (placeholder)
	@echo "No tests configured yet"

lint: ## Run linters
	flake8 . --max-line-length=100 --extend-ignore=E203
	mypy . --ignore-missing-imports || true

format: ## Format code with black and isort
	black .
	isort .

clean: ## Clean up generated files
	find . -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.log" -delete
	rm -rf reports/*.md 2>/dev/null || true
	rm -rf .pytest_cache 2>/dev/null || true
	rm -rf .mypy_cache 2>/dev/null || true

run: ## Run the application (example: make run COMPANY="Three Arrows Capital")
	@if [ -z "$(COMPANY)" ]; then echo "Usage: make run COMPANY='Company Name'"; exit 1; fi
	python main.py "$(COMPANY)"

run-verbose: ## Run with verbose logging
	@if [ -z "$(COMPANY)" ]; then echo "Usage: make run-verbose COMPANY='Company Name'"; exit 1; fi
	python main.py "$(COMPANY)" --verbose

streamlit: ## Run Streamlit web UI
	streamlit run app.py
