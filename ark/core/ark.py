
from ark.core.objects import Column
from ark.core.libs import SingletonMeta, delete_file, datas_files


class Ark(metaclass=SingletonMeta):
    def __init__(self):
        # at init Ark looking for columns files in 'database' directory
        # if files are found Ark create attributes of the same name.
        self._upload()

    def _upload(self):
        # looking for columns's file and create attribute for each one.
        files = datas_files()
        for i in files:
            if i.split('.')[0] != 'index':
                self.__add__(i.split('.')[0])

    """create column attribut"""
    def __add__(self, other):
        nwc = Column(other)
        setattr(self, other, nwc)

    """remove column attribut"""
    def __delete__(self, instance):
        self.__getattribute__(instance).close()
        delattr(self, instance)
        delete_file(instance)
