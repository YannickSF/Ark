
import unittest
from core.objects import Column

c = Column('test')


class TestColumn(unittest.TestCase):

    def test_create(self):
        c.cache.clear()

        self.assertEqual(c.name, 'test')
        self.assertIsNotNone(c.cache)

        self.assertEqual(c.cache, [])

    def test_insert(self):
        c.cache.clear()
        c.insert('id', object={'id': 'id1', 'key1': 'value1'})
        c.insert('id', object={'id': 'id2', 'key1': 'value2'})

        self.assertEqual(c.get('id', 'id1')[0], {'id': 'id1', 'key1': 'value1'})

    def test_get(self):
        c.cache.clear()
        c.insert('id', object={'id': 'id1', 'key1': 'value1'})
        c.insert('id', object={'id': 'id2', 'key1': 'value2'})
        c.insert('id', object={'id': 'id3', 'key1': 'value3'})
        c.insert('id', object={'id': 'id3', 'key1': 'value4'})

        values = c.get()
        obj1 = c.get('id', 'id1')
        obj2 = c.get('key1', 'value2')
        obj3 = c.get(query={'id': 'id3', 'key1': 'value3'})

        self.assertTrue(len(values) == 4)
        self.assertEqual({'id': 'id1', 'key1': 'value1'}, obj1[0])
        self.assertTrue(len(obj1) == 1)
        self.assertEqual({'id': 'id2', 'key1': 'value2'}, obj2[0])
        self.assertTrue(len(obj2) == 1)
        self.assertEqual({'id': 'id3', 'key1': 'value3'}, obj3[0])
        self.assertTrue(len(obj3) == 1)

    def test_update(self):
        c.cache.clear()
        c.insert('id', object={'id': 'id1', 'key1': 'value1'})

        c.update('id', 'id1', object={'id': 'id1', 'key1': 'NEW'})

        self.assertEqual({'id': 'id1', 'key1': 'NEW'}, c.get('id', 'id1')[0])

    def test_delete(self):
        c.cache.clear()
        c.insert('id', object={'id': 'id1', 'key1': 'value1'})
        c.insert('id', object={'id': 'id2', 'key1': 'value2'})

        c.delete('id', 'id1')

        self.assertTrue(len(c.cache) == 1)
        self.assertNotIn({'id': 'id1', 'key1': 'value1'}, c.cache)

    def test_commit(self):
        c.cache.clear()
        c.insert('id', object={'id': 'id1', 'key1': 'value1'})
        c.insert('id', object={'id': 'id2', 'key1': 'value2'})

        c.commit()
        self.assertTrue(True)

    def test_refresh(self):
        c.cache.clear()
        c.insert('id', object={'id': 'id1', 'key1': 'value1'})
        c.insert('id', object={'id': 'id2', 'key1': 'value2'})
        c.commit()
        c.update('id1', object={'id': 'id1', 'key1': 'NEW'})

        c.refresh()

        self.assertEqual([{'id': 'id1', 'key1': 'value1'}, {'id': 'id2', 'key1': 'value2'}], c.cache)


if __name__ == '__main__':
    unittest.main()
    c.close()
