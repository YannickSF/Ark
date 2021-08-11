
import unittest
from main import Ark
from core.libs import datas_files

a = Ark()


class TestArk(unittest.TestCase):

    def test_add(self):
        a.__add__('test_a')

        self.assertIsNotNone(a.test_a)

    def test_delete(self):
        a.__delete__('test_a')

        self.assertNotIn('test_a.json', datas_files())
