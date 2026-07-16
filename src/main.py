"""
main.py

Project Entry Point

This program demonstrates the complete data logging workflow:

1. Connect to the SQLite database.
2. Create the required table (if it does not already exist).
3. Read data from a virtual sensor.
4. Collect the measurement in a standardized format.
5. Store the measurement in the database.
6. Read all stored records.
7. Display the records on the console.

This file serves as a simple educational example for learning
how different software components interact together.
"""

from sensors.temperature_sensor import TemperatureSensor
from data_collector import DataCollector
from database.database import Database


# This example demonstrates one complete data logging cycle.
def main():

    db = Database()
    sensor = TemperatureSensor()
    collector = DataCollector()

    db.create_table()

    data = collector.collect(sensor)

    db.insert(data)

    rows = db.select_all()

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()