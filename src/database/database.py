import sqlite3


class Database:
    """
    Simple SQLite database manager.

    This class is responsible for:
    - Connecting to the SQLite database.
    - Creating the required table.
    - Inserting sensor data.
    - Retrieving stored records.
    - Performing simple database queries.

    Note:
        This implementation is intentionally simple because this project
        is an educational repository for learning the fundamentals of
        working with SQLite databases in Python.
    """

    def __init__(self,database_name):
        """
        Establish a connection to the SQLite database.

        If the database file does not exist, SQLite automatically creates it.
        A cursor object is also created for executing SQL commands.
        """

        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

        print("Database connected.")

    def create_table(self):
        """
        Create the sensor_data table.

        The 'IF NOT EXISTS' clause prevents an error if the table
        already exists.
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
        self.connection.commit()

        print("Table created.")

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

        Notes
        -----
        Parameterized queries (?) are used to improve safety and help
        prevent SQL injection.
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

        self.connection.commit()

        print("Data inserted successfully.")

    def select_all(self):
        """
        Retrieve all records from the sensor_data table.

        Returns
        -------
        list
            A list of tuples containing every stored record.
        """

        query = """
        SELECT *
        FROM sensor_data
        """

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        return rows

    def select_last(self):
        """
        Retrieve the most recently inserted record.

        Returns
        -------
        tuple
            The newest record.

        None
            If the table is empty.
        """

        query = """
        SELECT *
        FROM sensor_data
        ORDER BY id DESC
        LIMIT 1
        """

        self.cursor.execute(query)

        row = self.cursor.fetchone()

        return row

    def count_all(self):
        """
        Count the total number of records.

        Returns
        -------
        int
            Total number of stored records.
        """

        query = """
        SELECT COUNT(*)
        FROM sensor_data
        """

        self.cursor.execute(query)

        result = self.cursor.fetchone()

        return result[0]

    def average(self):
        """
        Calculate the average value of all stored measurements.

        Returns
        -------
        float
            Average measurement value.

        Notes
        -----
        Returns 0 if the table is empty.
        """

        query = """
        SELECT AVG(value)
        FROM sensor_data
        """

        self.cursor.execute(query)

        result = self.cursor.fetchone()

        return round(result[0], 2) if result[0] is not None else 0

    def delete_all(self):
        """
        Delete all records from the sensor_data table.

        Notes
        -----
        The table structure is preserved.
        Only the stored data is removed.
        """

        query = """
        DELETE FROM sensor_data
        """

        self.cursor.execute(query)

        self.connection.commit()

        print("All records deleted.")