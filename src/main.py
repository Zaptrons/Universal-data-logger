from sensors.temperature_sensor import TemperatureSensor
from data_collector import DataCollector
from database.database import Database

db = Database()
sensor = TemperatureSensor()
collector = DataCollector()
db.create_table()
data = collector.collect(sensor)
db.insert(data)
rows = db.select_all()

for row in rows:
    print(row)

