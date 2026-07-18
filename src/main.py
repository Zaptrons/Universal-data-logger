"""
main.py

Project Entry Point

This program demonstrates a complete data logging workflow.

Workflow
--------
1. Connect to the SQLite database.
2. Create the required table (if it does not already exist).
3. Read a value from a virtual sensor.
4. Collect the measurement into a standardized dictionary.
5. Store the measurement in the database.
6. Demonstrate the basic database query methods.
7. Display the results on the console.

This file is intentionally simple because it is part of an
educational project that teaches the fundamentals of Python,
SQLite, and clean project structure.
"""

from sensors.temperature_sensor import TemperatureSensor
from data_collector import DataCollector
from database.database import Database


def main():
    """
    Execute one complete data logging cycle.

    This function demonstrates how the main project components
    work together.
    """

    # Create the main project objects.
    db = Database()
    sensor = TemperatureSensor()
    collector = DataCollector()

    # Ensure the required table exists.
    db.create_table()

    # Collect one sensor measurement.
    data = collector.collect(sensor)

    # Store the measurement.
    db.insert(data)

    # Display all stored records.
    print("\nAll records:")
    rows = db.select_all()

    for row in rows:
        print(row)

    # Display the latest stored record.
    print("\nLast record:")
    print(db.select_last())

    # Display the total number of records.
    print("\nTotal records:")
    print(db.count_all())

    # Display the average measured value.
    print("\nAverage value:")
    print(db.average())


if __name__ == "__main__":
    main()