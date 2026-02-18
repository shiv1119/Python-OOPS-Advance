from enum import Enum

class LogLevel(Enum):
    INFO = 1
    DEBUG = 2
    ERROR = 3

class Logger:
    def __init__(self, file_name, level = LogLevel.INFO):
        if not file_name:
            raise ValueError("file_name is required")

        self.file_name = file_name
        if not isinstance(level, LogLevel):
            raise ValueError("Invalid log level")
        self.level = level

    @classmethod
    def from_config(cls, config_dict):
        file_name = config_dict.get("file_name")
        level_str = config_dict.get("level", "INFO")
        try:
            level = LogLevel[level_str]
        except KeyError:
            raise ValueError("Invalid log level")
        
        return cls(file_name, level)
    
config = {
    "file_name": "app.log",
    "level": "ERROR"
}

logger = Logger.from_config(config_dict = config)
print(logger.file_name, logger.level)
