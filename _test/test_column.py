
import unittest
from core.objects import Column
from core.libs import delete_file

c = Column('test')


class TestColumn(unittest.TestCase):

    def test_create(self):
        c.cache.clear()

        self.assertEqual(c.name, 'test')
        self.assertIsNotNone(c.cache)

        self.assertEqual([k for k in c.cache.keys()], [])

    def test_insert(self):
        c.insert(object={'id': 'id1', 'key1': 'value1'})
        c.insert(object={'id': 'id2', 'key2': 'value2'})

        self.assertEqual(c.cache['id1'], {'id': 'id1', 'key1': 'value1'})

    def test_get(self):
        c.insert(object={'id': 'id1', 'key1': 'value1'})
        c.insert(object={'id': 'id2', 'key2': 'value2'})

        values = c.get()
        obj1 = c.get('id1', property='id')

        self.assertTrue(len(values) == 2)
        self.assertEqual({'id': 'id1', 'key1': 'value1'}, obj1[0])

    def test_update(self):
        c.insert(object={'id': 'id1', 'key1': 'value1'})

        c.update('id1', object={'id': 'id1', 'key1': 'NEW'})

        self.assertEqual({'id': 'id1', 'key1': 'NEW'}, c.cache['id1'])

    def test_delete(self):
        c.insert(object={'id': 'id1', 'key1': 'value1'})
        c.insert(object={'id': 'id2', 'key2': 'value2'})

        c.delete('id1')

        self.assertTrue(len(c.cache) == 1)
        self.assertNotIn({'id': 'id1', 'key1': 'value1'}, [c.cache[k] for k in c.cache.keys()])

    def test_commit(self):
        c.insert(object={'id': 'id1', 'key1': 'value1'})
        c.insert(object={'id': 'id2', 'key2': 'value2'})

        c.commit()
        self.assertTrue(True)

    def test_refresh(self):
        c.insert(object={'id': 'id1', 'key1': 'value1'})
        c.insert(object={'id': 'id2', 'key2': 'value2'})
        c.commit()
        c.update('id1', object={'id': 'id1', 'key1': 'NEW'})

        c.refresh()

        self.assertEqual([{'id': 'id1', 'key1': 'value1'}, {'id': 'id2', 'key2': 'value2'}],
                         [c.cache[k] for k in c.cache.keys()])


if __name__ == '__main__':
    unittest.main()
    c.close()
