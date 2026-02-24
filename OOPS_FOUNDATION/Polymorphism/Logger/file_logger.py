from .base_logger import Logger
class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename
        self.logs = []

    def log(self, message):
        entry = f"[FILE] {message}"
        self.logs.append(entry)
        print(f"Writing to {self.filename}: {entry}")

    def __add__(self, other):
        combined = FileLogger("combined_file.txt")
        combined.logs = self.logs + other.logs
        return combined

    def __eq__(self, other):
        return self.logs == other.logs
    

    