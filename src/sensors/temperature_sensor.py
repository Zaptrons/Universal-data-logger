from .sensor import Sensor
import random

class TemperatureSensor(Sensor):
    def get_name(self):
        return "Temperature"
    
    def read(self):
        return round(random.uniform(25,40),1)

    def get_unit(self):
        return "°C"
        
