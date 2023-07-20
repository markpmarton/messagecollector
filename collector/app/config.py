import os

# database connection string
DB_CONN_STR = f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_CONTAINER_NAME")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
# template for log messages (in /app/logs.log by default)
LOG_FORMAT = (
    "%(asctime)s|%(filename)s|%(levelname)s|%(funcName)s:%(lineno)s|%(message)s"
)
# relative path of the log file from the working directory
LOG_PATH = "logs.log"
LOG_WORK_DIR = "/app"
