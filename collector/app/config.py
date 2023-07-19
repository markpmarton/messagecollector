import os

DB_CONN_STR = f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_CONTAINER_NAME")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
