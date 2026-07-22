"""
main.py

Project Entry Point

This module demonstrates one complete data logging cycle.

Workflow
--------
1. Load the project configuration from a JSON file.
2. Connect to the SQLite database.
3. Create the required table (if it does not already exist).
4. Create the configured sensor object.
5. Collect one measurement.
6. Store the measurement in the database.
7. Retrieve and display all stored records.

This file intentionally remains simple because the goal of this
project is educational rather than building a production-ready
application.
"""

from config_loader import ConfigLoader
from database.database import Database
from data_collector import DataCollector
from sensors.temperature_sensor import TemperatureSensor


def main():
    """
    Run one complete data logging cycle.

    This function coordinates the main application workflow:
    configuration loading, sensor creation, data collection,
    database storage, and displaying the stored records.
    """

    # ---------------------------------------------------------
    # Load project configuration.
    # ---------------------------------------------------------
    loader = ConfigLoader()
    config = loader.load()

    # ---------------------------------------------------------
    # Create database using the configured database file.
    # ---------------------------------------------------------
    db = Database(config["database"])

    # ---------------------------------------------------------
    # Create the configured sensor.
    # Future milestones will support multiple sensor types.
    # ---------------------------------------------------------
    if config["sensor"] == "Temperature":
        sensor = TemperatureSensor()
    else:
        raise ValueError("Unknown sensor type.")

    # ---------------------------------------------------------
    # Collect one measurement from the sensor.
    # ---------------------------------------------------------
    collector = DataCollector()
    data = collector.collect(sensor)

    # ---------------------------------------------------------
    # Store the measurement.
    # ---------------------------------------------------------
    db.create_table()
    db.insert(data)

    # ---------------------------------------------------------
    # Display all stored records.
    # ---------------------------------------------------------
    print("\nStored Records\n")

    rows = db.select_all()

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()