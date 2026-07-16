import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("sensor_data.db")
        self.cursor = self.connection.cursor()
        print("Database Connected.")


    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor TEXT NOT NULL,
            value REAL NOT NULL,
            unit TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
        """
        self.cursor.execute(query)
        self.connection.commit()
        print("Table Created.")

    def insert(self, data):
        query = """
        INSERT INTO sensor_data
        (sensor, value, unit, timestamp)
        VALUES (?, ?, ?, ?)
        """
        self.cursor.execute(
            query,
            (
                data["sensor"],
                data["value"],
                data["unit"],
                data["timestamp"]
            )
        )
        self.connection.commit()
        print("Data inserted successfully.")

    def select_all(self):
        query = "SELECT * FROM sensor_data"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows