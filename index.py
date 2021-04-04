
from core.libs import SingletonMeta
from core.objects import Column


class Ark(metaclass=SingletonMeta):
    def __init__(self):
        self._attributes = []

    def _upload(self):
        # looking for column's file and create attribute for each one.
        pass

    def add(self, name):
        nct = Column(name)
        setattr(self, name, nct)
        self._attributes.append(name)

    def put(self, name, other):
        # alter table name.
        pass

    def remove(self, name):
        # drop table.
        delattr(self, name)
        # remove file after attribute remove.
        self._attributes.remove(name)

    def commit(self):
        # save cache tables.
        for a in self._attributes:
            self[a].commit()
        return True

    def refresh(self):
        # restore cache from tables.
        for a in self._attributes:
            self[a].refresh()
        return True
