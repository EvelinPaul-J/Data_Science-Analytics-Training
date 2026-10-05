from collections import OrderedDict
class DataBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()
    def get(self, key):
        if key in self.data:
            value = self.data[key]
            self.data.move_to_end(key)
            return value
        return None
    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)
buffer = DataBuffer(2)
buffer.put("sensor1", 24.5)
buffer.put("sensor2", 28.0)
buffer.get("sensor1")
buffer.put("sensor3", 31.2)
print(buffer.get("sensor2"))
print(buffer.get("sensor1"))
print(buffer.get("sensor3"))