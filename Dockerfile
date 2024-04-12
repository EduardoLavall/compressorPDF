# syntax=docker/dockerfile:1

FROM python:latest 

WORKDIR /app

RUN apt-get update \
    && apt-get install -y ghostscript \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP app.py

COPY requirements.txt requirements.txt

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]