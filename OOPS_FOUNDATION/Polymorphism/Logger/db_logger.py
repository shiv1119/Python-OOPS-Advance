from .base_logger import Logger

class DBLogger(Logger):
    def __init__(self, db_name):
        self.db_name = db_name
        self.logs = []
    
    def log(self, message):
        entry = f"[DB] {message}"
        self.logs.append(entry)
        print(f"Inserting into {self.db_name}: {entry}")

    def __add__(self, other):
        combined = DBLogger("combined_db")
        combined.logs = self.logs + other.logs
        return combined
    
    def __eq__(self, other):
        return self.logs == other.logs
    