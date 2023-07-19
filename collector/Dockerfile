
FROM tiangolo/uvicorn-gunicorn:python3.11

LABEL author="Mark Marton"
LABEL description="Collector service for the messagecollector"
LABEL version="1.0"

RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy psycopg2-binary

COPY ./app /app
WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
