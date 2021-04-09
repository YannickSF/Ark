
from core.nosql import Table


class Column:
    def __init__(self, name):
        self.name = name
        self.table = Table(name)
        self.cache = []

        self._upload()

    def _upload(self):
        data = self.table.all()
        if len(data) > 0:
            self.refresh()

    """ 
    @arg.0 -> property to watching on
    @arg.1 -> value to search
    """
    def _find(self, *args, **kwargs):
        def shake(rec_list, qproperty, qvalue):
            return list(filter(lambda x: x[qproperty] == qvalue, rec_list))

        n_tab = self.cache

        if len(args) == 2:
            n_tab = shake(n_tab, args[0], args[1])
        elif len(args) == 0 & kwargs.keys().__contains__('query'):
            for key in kwargs['query']:
                n_tab = shake(n_tab, key, kwargs['query'][key])

        return n_tab

    """
        @args .0 -> propety to filter
        @args .1 -> value to filter
        @kwargs .query -> query dict of values
        """
    def get(self, *args, **kwargs):
        if len(args) == 2:
            return self._find(args[0], args[1])
        elif len(args) == 0 and kwargs.keys().__contains__('query'):
            return self._find(**kwargs)
        return self.cache

    """
    @kwargs .object -> object to insert
    """
    def insert(self, *args, **kwargs):
        self.cache.append(kwargs['object'])

    """
    @args .0 -> propety to filter
    @args .1 -> value to filter
    @kwargs .uobject -> object for update
    """
    def update(self, *args, **kwargs):
        if len(args) == 2 and kwargs.keys().__contains__('object'):
            idx = self.cache.index(self._find(args[0], args[1])[0])
            self.cache[idx] = kwargs['object']
            return self.cache[idx]
        return None

    """
        @args .0 -> propety to filter
        @args .1 -> value to filter
    """
    def delete(self, *args, **kwargs):
        if len(args) == 2:
            idx = self.cache.index(self._find(args[0], args[1])[0])
            self.cache.remove(self.cache[idx])

    """commiting cache to files."""
    def commit(self):
        self.table.purge_table(self.name)
        for i in self.cache:
            self.table.insert(i)
        return True

    """reload cache from files."""
    def refresh(self):
        self.cache = self.table.all()

    """close access to file."""
    def close(self):
        self.table.close()


class SynergyReponse:
    def __init__(self, **kwargs):
        pass

    def __repr__(self):
        return {}

    def __str__(self):
        return self.__repr__().__str__()


class SyObject:
    def __init__(self, **kwargs):
        pass

    def __repr__(self):
        return {}

    def __str__(self):
        return self.__repr__().__str__()
