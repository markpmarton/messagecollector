import os

DB_CONN_STR = f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_CONTAINER_NAME")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
MIN_TIME = "2000-01-01T00:00:00.000"
