class MemoryStorage:
    def __init__(self):
        self._data = {}

    def create(self, key, value):
        self._data[key] = value
        return True

    def read(self, key):
        return self._data.get(key)

    def update(self, key, value):
        if key in self._data:
            self._data[key] = value
            return True
        return False

    def delete(self, key):
        if key in self._data:
            del self._data[key]
            return True
        return False

    def read_all(self):
        return self._data
