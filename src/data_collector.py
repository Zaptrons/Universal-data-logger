from datetime import datetime


class DataCollector:
    

    def collect(self,sensor):
        data = {
           "sensor": sensor.get_name(),
           "value": sensor.read(),
           "unit": sensor.get_unit(),
           "timestamp": datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        }

        return data