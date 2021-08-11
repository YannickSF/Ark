
from settings import SETTINGS
from core.libs import SingletonMeta
from core.objects import Table
from tinydb import Query


class ArkIndex(Table, metaclass=SingletonMeta):
    def __init__(self):
        Table.__init__(self, SETTINGS.INDEX_DATABASE_PATH + '/arkindex')

    """ upsert value in index database"""
    def capture(self, value, doc_id=-1):
        """ 0 : column_index in database , @... relateds value for capture"""
        return self.upsert(value, Query()['doc_id'] == doc_id)
