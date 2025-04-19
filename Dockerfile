## For more information, please refer to https://aka.ms/vscode-docker-python
#FROM python:3.9-slim
#
## Install build tools and dependencies for pandas and other packages
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends gcc g++ libpq-dev build-essential && \
#    rm -rf /var/lib/apt/lists/*
#
#COPY requirements.txt .
#RUN python -m pip install --upgrade pip
#RUN python -m pip install -r requirements.txt
#
#WORKDIR /app
#COPY Recomender /app
#
#EXPOSE 5002
#
## Keeps Python from generating .pyc files in the container
#ENV PYTHONDONTWRITEBYTECODE=1
#
## Turns off buffering for easier container logging
#ENV PYTHONUNBUFFERED=1
#
## Install pip requirements
#COPY requirements.txt .
#RUN python -m pip install -r requirements.txt
#
#WORKDIR /app
#COPY Recomender /app
#
## Creates a non-root user with an explicit UID and adds permission to access the /app folder
## For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser
#
## During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["gunicorn", "--bind", "0.0.0.0:5002", "app:app"]


# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Install build tools and dependencies for pandas and other packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc g++ libpq-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install --upgrade pip setuptools wheel && \
    python -m pip install -r requirements.txt

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Copy project files
COPY app.py .
COPY recommendation.py .
COPY model.pkl .
COPY similarity.pkl .
COPY tmdb_5000_credits.csv .
COPY tmdb_5000_movies.csv .
COPY Recomender.sln .
COPY templates/ /app/templates/
#COPY .dockerignore .

EXPOSE 5002

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden
CMD ["gunicorn", "--bind", "0.0.0.0:5002", "app:app"]