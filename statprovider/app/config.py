import os

DB_CONN_STR = f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_CONTAINER_NAME")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
TIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
MIN_TIME = "2000-01-01T00:00:00"
LOG_FORMAT = (
    "%(asctime)s|%(filename)s|%(levelname)s|%(funcName)s:%(lineno)s|%(message)s"
)
LOG_PATH = "logs.log"
LOG_WORK_DIR = "/app"
