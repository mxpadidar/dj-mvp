.PHONY: all install run migrations migrate lint format type-check
all: install lint type-check
	@echo "-> all checks passed!"

install:
	@uv sync

run:
	@uv run manage.py runserver

migrations:
	@uv run manage.py makemigrations

migrate:
	@uv run manage.py migrate

superuser:
	@uv run manage.py createsuperuser

lint:
	@uv run ruff format .

format:
	@uv run ruff check .

type-check:
	@uv run pyright .
