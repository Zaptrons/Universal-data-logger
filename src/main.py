from sensors.temperature_sensor import TemperatureSensor
from data_collector import DataCollector


sensor = TemperatureSensor()
collector = DataCollector()

data = collector.collect(sensor)

print(f"Sensor   : {data['sensor']}")
print(f"Value    : {data['value']} {data['unit']}")
print(f"Timestamp: {data['timestamp']}")
