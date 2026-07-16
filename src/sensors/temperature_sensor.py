from .sensor import Sensor
import random


class TemperatureSensor(Sensor):
    """
    Virtual temperature sensor.

    This class simulates a real temperature sensor by generating
    random values within a predefined range.

    It is used only for learning and testing purposes until
    a real hardware sensor is connected.
    """

    def get_name(self):
        """
        Return the sensor name.

        Returns
        -------
        str
            Sensor name.
        """
        return "Temperature"
    
    # NOTE:
    # Replace this simulated value with real sensor data
    # when hardware becomes available.
    def read(self):
        """
        Simulate a temperature measurement.

        Returns
        -------
        float
            Random temperature between 25.0 °C and 40.0 °C
            rounded to one decimal place.
        """
        return round(random.uniform(25, 40), 1)

    def get_unit(self):
        """
        Return the engineering unit.

        Returns
        -------
        str
            Temperature unit (degrees Celsius).
        """
        return "°C"