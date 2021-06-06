
from core.libs import SingletonMeta, delete_file, datas_files
from core.objects import Column


class Ark(metaclass=SingletonMeta):
    def __init__(self):
        # at init Ark looking for columns files in 'datas' directory
        # if files are found Ark create column attributs and upload data to cache
        self._attributes = []
        self._columns = {}
        self._upload()

    def _upload(self):
        # looking for columns's file and create attribute for each one.
        files = datas_files()
        for i in files:
            self.__add__(i.split('.')[0])

    """create column attribut"""
    def __add__(self, other):
        nwc = Column(other)
        setattr(self, other, nwc)
        self._attributes.append(other)
        self._columns[other] = nwc

    def alter(self, *args, **kwargs):
        if args[0] == 'rename':
            self.__add__(args[2])
            for it in self._columns[args[1]].all:
                self._columns[args[2]].insert(it)

    """remove column attribut"""
    def __delete__(self, instance):
        delattr(self, instance)
        delete_file(instance)
        self._attributes.remove(instance)
        del self._columns[instance]

    def index(self):

        class ArkIndex:
            """ Parameters [0] must be Ark db instance """
            def __init__(self, *args, **kwargs):
                self.mapping = {}
                # persister le mapping  

            def __add__(self, other):
                pass

            def __delete__(self, instance):
                pass

        return ArkIndex(self)

    """provide query on all columns at one time """
    def search(self, parameters, query):

        class ArkQuery:
            def __init__(self, *args, **kwargs):
                self.parameters = args
                self.query = kwargs

                self._execute()

            def _execute(self):
                pass

            def fetch(self):
                return

        return ArkQuery(self, parameters, kwargs=query)
