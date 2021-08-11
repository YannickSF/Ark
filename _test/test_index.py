
import unittest
from main import ArkIndex
from core.nosql import Query


i = ArkIndex()


class TestArkIndex(unittest.TestCase):

    def test_capture(self):
        obj = {'id': 1, 'key1': 'lol', 'key2': '002'}
        i.capture(obj)

        self.assertTrue(len(i.search(Query()['id'] == 1)) == 1)
