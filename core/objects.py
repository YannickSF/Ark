
from core.nosql import Table, Query


class Column:
    def __init__(self, name):
        self.name = name
        self.table = Table(name)
        self.cache = {}

        self._upload()

    def _upload(self):
        data = self.table.all()
        if len(data) > 0:
            self.refresh()

    def _find(self, *args, **kwargs):
        # todo : EVOLUTION -> prendre plusieurs propriétées en charge pour la recherche.
        return list(filter(lambda x: x[kwargs['property']] == args[0], [self.cache[k] for k in self.cache.keys()]))

    def get(self, *args, **kwargs):
        if len(args) > 0:
            return self._find(args[0], property=kwargs['property'])
        return self.cache

    def insert(self, *args, **kwargs):
        # todo : EVOLUTION -> primaryKey au choix.
        self.cache[kwargs['object']['id']] = kwargs['object']

    def update(self, *args, **kwargs):
        if args[0] is not None:
            self.cache[args[0]] = kwargs['object']
            return self.cache[args[0]]
        return None

    def delete(self, *args, **kwargs):
        if args[0] is not None:
            del self.cache[args[0]]

    """commit des informations du cache en dur"""
    def commit(self):
        self.table.purge_table(self.name)
        for k in self.cache.keys():
            self.table.insert(self.cache[k])
        return True

    """rechargement des données du cache depuis les données en durs"""
    def refresh(self):
        data = self.table.all()
        self.cache = {o['id']: o for o in data}

    def close(self):
        self.table.close()
