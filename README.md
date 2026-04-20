# generation-health-reports

A service for collecting, analyzing, and generating personalized health reports. Supports PDF export and email delivery.

## Features

- Collect health data: sleep, stress, activity, chronic conditions
- Detect deviations from norm
- Generate weekly and monthly reports
- Export reports as PDF
- Send reports via email
- Store report history

## Tech Stack

- Python 3.12+
- [FastAPI](https://fastapi.tiangolo.com/) — async REST API
- PostgreSQL — primary database
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM
- [Pydantic](https://docs.pydantic.dev/) — data validation
- [Typer](https://typer.tiangolo.com/) — CLI interface
- Docker + Docker Compose
- Poetry — dependency management

## Getting Started

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation)
- Docker and Docker Compose

### Installation

```bash
git clone https://github.com/vevdokimovm/generation-health-reports.git
cd generation-health-reports
poetry install
```

### Environment

Copy the example env file and fill in the values:

```bash
cp .env.example .env
```

### Run with Docker

```bash
docker-compose up --build
```

### Run locally

```bash
# Start PostgreSQL separately, then:
poetry run uvicorn src.main:app --reload
```

### CLI

```bash
poetry run python -m cli.main --help
```

## Project Structure

```
generation-health-reports/
├── cli/                  # CLI entry points
├── src/
│   ├── domain/           # Business logic
│   ├── entities/         # Domain models
│   ├── infra/            # Infrastructure (DB, API, routers)
│   └── settings/         # Configuration
├── tests/                # Test suite
├── docker-compose.yml
├── Dockerfile
└── pyproject.toml
```

## Development

```bash
# Run tests
poetry run pytest

# Lint
poetry run ruff check .
```

## License

MIT
