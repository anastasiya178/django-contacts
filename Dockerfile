FROM python:3.11

ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Set environment variable to bypass PEP 517 for mysqlclient
ENV PIP_NO_USE_PEP517=1
ENV POETRY_VIRTUALENVS_CREATE=false

# Copy poetry files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false \
 && poetry install --no-root

# Set the working directory in the container
WORKDIR /django-contacts

# Copy the dependency specification files into the container
COPY . .

RUN poetry show -v
RUN poetry install

