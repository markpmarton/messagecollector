import logging
import os

from config import LOG_PATH, LOG_FORMAT, LOG_WORK_DIR


class LoggerFactory:
    @staticmethod
    def __create_logger(log_path, level, working_dir, format):
        formatter = logging.Formatter(format)

        full_log_path = os.path.join(working_dir, log_path)

        LoggerFactory._level = level
        LoggerFactory._log_path = full_log_path
        LoggerFactory._logger = logging.getLogger("messagecollector_collector_logger")

        logging.basicConfig(
            level=logging.INFO, format=format, datefmt="%Y-%m-%d %H:%M:%S"
        )

        match level:
            case "INFO":
                LoggerFactory._logger.setLevel(logging.INFO)
            case "ERROR":
                LoggerFactory._logger.setLevel(logging.ERROR)
            case "DEBUG":
                LoggerFactory._logger.setLevel(logging.DEBUG)
            case "WARNING":
                LoggerFactory._logger.setLevel(logging.WARNING)
            case "CRITICAL":
                LoggerFactory._logger.setLevel(logging.CRITICAL)

        file_handler = logging.FileHandler(full_log_path)
        file_handler.setLevel(LoggerFactory._logger.level)
        file_handler.setFormatter(formatter)
        LoggerFactory._logger.addHandler(file_handler)

        return LoggerFactory._logger

    @staticmethod
    def get_logger():
        logger = LoggerFactory.__create_logger(
            LOG_PATH, "INFO", LOG_WORK_DIR, LOG_FORMAT
        )
        return logger


Logger = LoggerFactory.get_logger()
