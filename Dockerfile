# Use the official Python 3.11 image as the base image
FROM python:3.11

# Set an environment variable to ensure output is not buffered (useful for logging)
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential      # Essential build tools (e.g., GCC)

# Install Poetry (a dependency management and packaging tool)
RUN curl -sSL https://install.python-poetry.org | python3 -
# Add Poetry to the PATH environment variable
ENV PATH="/root/.local/bin:$PATH"

# Set environment variable to bypass PEP 517 for mysqlclient
ENV PIP_NO_USE_PEP517=1

# Copy the Poetry configuration files to the container
COPY pyproject.toml poetry.lock ./

# Install project dependencies without creating a virtual environment
RUN poetry config virtualenvs.create false \
 && poetry install --no-root

# Set the working directory in the container
WORKDIR /django-contacts

# Copy the entire project directory into the container
COPY . .
