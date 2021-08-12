
import unittest
from ark.core.objects import Column

c = Column('test')


class TestColumn(unittest.TestCase):

    def test_create(self):
        c.cache.clear()

        self.assertEqual(c.name, 'test')
        self.assertIsNotNone(c.cache)

        self.assertEqual(c.cache, [])

    def test_insert(self):
        c.cache.clear()
        c.cache_insert('id', object={'id': 'id1', 'key1': 'value1'})
        c.cache_insert('id', object={'id': 'id2', 'key1': 'value2'})

        self.assertEqual(c.cache_get('id', 'id1')[0], {'id': 'id1', 'key1': 'value1'})

    def test_get(self):
        c.cache.clear()
        c.cache_insert('id', object={'id': 'id1', 'key1': 'value1'})
        c.cache_insert('id', object={'id': 'id2', 'key1': 'value2'})
        c.cache_insert('id', object={'id': 'id3', 'key1': 'value3'})
        c.cache_insert('id', object={'id': 'id3', 'key1': 'value4'})

        values = c.cache_get()
        obj1 = c.cache_get('id', 'id1')
        obj2 = c.cache_get('key1', 'value2')
        obj3 = c.cache_get(query={'id': 'id3', 'key1': 'value3'})

        self.assertTrue(len(values) == 4)
        self.assertEqual({'id': 'id1', 'key1': 'value1'}, obj1[0])
        self.assertTrue(len(obj1) == 1)
        self.assertEqual({'id': 'id2', 'key1': 'value2'}, obj2[0])
        self.assertTrue(len(obj2) == 1)
        self.assertEqual({'id': 'id3', 'key1': 'value3'}, obj3[0])
        self.assertTrue(len(obj3) == 1)

    def test_update(self):
        c.cache.clear()
        c.cache_insert('id', object={'id': 'id1', 'key1': 'value1'})

        c.cache_update('id', 'id1', object={'id': 'id1', 'key1': 'NEW'})

        self.assertEqual({'id': 'id1', 'key1': 'NEW'}, c.cache_get('id', 'id1')[0])

    def test_delete(self):
        c.cache.clear()
        c.cache_insert('id', object={'id': 'id1', 'key1': 'value1'})
        c.cache_insert('id', object={'id': 'id2', 'key1': 'value2'})

        c.cache_delete('id', 'id1')

        self.assertTrue(len(c.cache) == 1)
        self.assertNotIn({'id': 'id1', 'key1': 'value1'}, c.cache)

    def test_commit(self):
        c.cache.clear()
        c.cache_insert('id', object={'id': 'id1', 'key1': 'value1'})
        c.cache_insert('id', object={'id': 'id2', 'key1': 'value2'})

        c.commit()
        self.assertTrue(True)

    def test_refresh(self):
        c.purge_tables()
        c.cache.clear()
        c.cache_insert('id', object={'id': 'id1', 'key1': 'value1'})
        c.cache_insert('id', object={'id': 'id2', 'key1': 'value2'})
        c.commit()
        c.cache_update('id', 'id1', object={'id': 'id1', 'key1': 'NEW'})

        c.refresh()

        self.assertEqual([{'id': 'id1', 'key1': 'value1'}, {'id': 'id2', 'key1': 'value2'}], c.cache)


if __name__ == '__main__':
    unittest.main()
    c.close()
