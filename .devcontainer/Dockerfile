# Use a base image with Python 3.12
FROM mcr.microsoft.com/devcontainers/python:3.12

# Set the working directory inside the container
WORKDIR /workspace

# Install system dependencies including OpenSSL and Python development packages
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    python3-dev \
    libffi-dev \
    libssl-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the PATH for the vscode user
ENV PATH="/home/vscode/.local/bin:$PATH"

# Switch to the 'vscode' user
USER vscode

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Install pre-commit
RUN pip install pre-commit

# Create a shell entry point for bash
ENTRYPOINT ["/bin/bash"]
