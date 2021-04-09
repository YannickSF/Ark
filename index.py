
from core.libs import SingletonMeta, delete_file, datas_files
from core.objects import Column


class Ark(metaclass=SingletonMeta):
    def __init__(self):
        # at init Ark looking for columns files in 'datas' directory
        # if files are found Ark create column attributs and upload data to cache
        self._attributes = []
        self._upload()

    def _upload(self):
        # looking for columns's file and create attribute for each one.
        files = datas_files()
        for i in files:
            self.add(i.split('.')[0])

    """create column attribut"""
    def add(self, name):
        setattr(self, name, Column(name))
        self._attributes.append(name)

    def put(self, *args, **kwargs):
        # todo : alter column
        pass

    """remove column attribut"""
    def remove(self, name):
        delattr(self, name)
        delete_file(name)
        self._attributes.remove(name)

    """make query on all column"""
    @property
    def query(self, **kwargs):

        class Synergy:
            def __init__(self, ark, args):
                self.ark = ark
                self.args = args

            def get(self):
                # get data -> column.selected(propeties)
                # return iterated(object.of(Dict))
                pass

        return Synergy(self, **kwargs)
