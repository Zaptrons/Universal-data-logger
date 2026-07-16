class Sensor:
    """
    Abstract base class for all sensors.

    Every sensor used in this project must inherit from this class
    and implement the required methods.

    The purpose of this interface is to ensure that all sensors expose
    a common API, allowing the DataCollector to work with any sensor
    without knowing its internal implementation.
    """

    def read(self):
        """
        Read the current value from the sensor.

        Returns
        -------
        float
            Current measured value.

        This method must be implemented by every derived sensor class.
        """
        raise NotImplementedError("read() must be implemented.")

    def get_unit(self):
        """
        Return the engineering unit of the sensor.

        Examples
        --------
        °C
        V
        A
        %

        This method must be implemented by every derived sensor class.
        """
        raise NotImplementedError("get_unit() must be implemented.")

    def get_name(self):
        """
        Return the sensor name.

        Examples
        --------
        Temperature
        Voltage
        Current
        Humidity

        This method must be implemented by every derived sensor class.
        """
        raise NotImplementedError("get_name() must be implemented.")