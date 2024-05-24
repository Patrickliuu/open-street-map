FROM python:3.10-slim-buster

# Prevents Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turn off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

EXPOSE 14032

WORKDIR /app
COPY . /app

CMD  ["python", "server.py"]