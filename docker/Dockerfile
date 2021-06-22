FROM python:3.7-alpine

RUN pip install elasticsearch

WORKDIR /app/
COPY docker/ingest.py /app/
COPY docker/setup.json /app/
CMD ["python", "ingest.py"]
