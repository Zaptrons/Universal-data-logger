import sqlite3


class Database:
    """
    Simple SQLite database manager.

    This class is responsible for:
    - Connecting to the SQLite database.
    - Creating the required tables.
    - Storing sensor data.
    - Reading stored records.

    Note:
        This implementation is intentionally simple because this project
        is a learning repository for understanding the fundamentals of
        working with databases in Python.
    """

    def __init__(self):
        """
        Establish a connection to the SQLite database.

        If the database file does not exist, SQLite automatically creates it.
        A cursor object is also created for executing SQL commands.
        """

        self.connection = sqlite3.connect("sensor_data.db")
        self.cursor = self.connection.cursor()

        print("Database Connected.")

    def create_table(self):
        """
        Create the sensor_data table.

        The 'IF NOT EXISTS' clause prevents an error if the table has
        already been created in a previous execution.
        """

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

        # Save changes permanently to the database file.
        self.connection.commit()

        print("Table Created.")

    def insert(self, data):
        """
        Insert a new sensor record into the database.

        Parameters
        ----------
        data : dict
            Dictionary containing:
                sensor
                value
                unit
                timestamp

        Parameterized queries (?) are used to improve safety and prevent
        SQL injection.
        """

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

        # Commit writes the inserted record to disk.
        self.connection.commit()

        print("Data inserted successfully.")

    def select_all(self):
        """
        Retrieve all records from the sensor_data table.

        Returns
        -------
        list
            List of tuples representing every stored record.
        """

        query = "SELECT * FROM sensor_data"

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        return rows