class Sensor:
    def read(self):
        raise NotImplementedError("get_read() must be impelemented.")
    def get_unit(self):
        raise NotImplementedError("get_unit() must be impelemented.")
    def get_name(self):
        raise NotImplementedError("get_name() must be impelemented.")