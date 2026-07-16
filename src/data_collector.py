from datetime import datetime


class DataCollector:
    """
    Collect sensor measurements and convert them into a
    standardized dictionary format.

    The DataCollector does not know how a sensor works.
    It only requests the required information through the
    common Sensor interface and prepares the data for storage.
    """

    def collect(self, sensor):
        """
        Collect a single measurement from the specified sensor.

        Parameters
        ----------
        sensor : Sensor
            Any object derived from the Sensor base class.

        Returns
        -------
        dict
            Dictionary containing:

            - sensor : Sensor name
            - value : Measured value
            - unit : Engineering unit
            - timestamp : Date and time of measurement

        Notes
        -----
        The timestamp is generated at the moment the measurement
        is collected, not when it is stored in the database.
        """

        data = {
            "sensor": sensor.get_name(),
            "value": sensor.read(),
            "unit": sensor.get_unit(),
            "timestamp": datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        }

        return data