from Logger.file_logger import FileLogger
from Logger.db_logger import DBLogger

def process_logs(logger):
    logger.log("System started")
    logger.log("User logged in")

file_logger = FileLogger("app.log")
db_logger = DBLogger("users_db")

# file_logger.log("System Started")
# file_logger.log("User logged in")

process_logs(file_logger)
process_logs(db_logger)