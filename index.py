
from core.libs import SingletonMeta, delete_file, datas_files
from core.objects import Column


class Ark(metaclass=SingletonMeta):
    def __init__(self):
        self._attributes = []
        self._upload()

    def _upload(self):
        # looking for columns's file and create attribute for each one.
        files = datas_files()
        for i in files:
            self.add(i.split('.')[0])

    def add(self, name):
        setattr(self, name, Column(name))
        self._attributes.append(name)

    def remove(self, name):
        delattr(self, name)
        delete_file(name)
        self._attributes.remove(name)
