PYTHON_BINARY := python3
VIRTUAL_ENV := env
VIRTUAL_BIN := $(VIRTUAL_ENV)/bin
PROJECT_NAME := news-scraper
TEST_DIR := test

## run - Execute the module
run:
	$(VIRTUAL_BIN)/python3 $(PROJECT_NAME)/news_scraper.py

## format - Runs all formatting tools against the project
format: black mypy

## lint - Lint the project
lint:
	$(VIRTUAL_BIN)/flake8 $(PROJECT_NAME)/ $(TEST_DIR)/

## black - Runs the Black Python formatter against the project
black:
	$(VIRTUAL_BIN)/black $(PROJECT_NAME)/ $(TEST_DIR)/

## black-check - Checks if the project is formatted correctly against the Black rules
black-check:
	$(VIRTUAL_BIN)/black $(PROJECT_NAME)/ $(TEST_DIR)/ --check

## mypy - Run mypy type checking on the project
mypy:
	$(VIRTUAL_BIN)/mypy $(PROJECT_NAME)/ $(TEST_DIR)/

## test - Test the project
test:
	$(VIRTUAL_BIN)/pytest