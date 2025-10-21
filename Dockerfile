# Use the official PostgreSQL image as a base
FROM python:3.12-slim

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD otree prodserver