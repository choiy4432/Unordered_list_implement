class Node:
    def __init__(self, name, data):
        assert isinstance(name, str)
        self.name = name
        self.data = data
        self.prev = None

    @property
    def name(self):
        return self._name

    @property
    def data(self):
        return self._data

    @property
    def prev(self):
        return self._prev

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @name.setter
    def name(self, new_name):
        assert isinstance(new_name, str)
        self._name = new_name

    @prev.setter
    def prev(self, new_prev):
        self._prev = new_prev
