import datetime
from copy import deepcopy


class File:
    def __init__(self, name, content):
        assert isinstance(name, str)
        assert isinstance(content, str)
        self.name = name
        self.date = datetime.datetime.now()
        self.edit_date = self.date
        self.content = content

    def __repr__(self):
        return f"Filename : {self.name}\nContent : {self.content}\nGenerated at {self.date:%Y-%m-%d %H:%M:%S}, Edited at {self.edit_date:%Y-%m-%d %H:%M:%S}"

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        assert isinstance(content, str)
        self._content = content
        self.edit_date = datetime.datetime.now()
        print(f"{self.edit_date - self.date} pass after generation")
