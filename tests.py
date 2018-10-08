import unittest
from DoubleLinkedList import DoubleLinkedList as dll


class TestDoubleLinkedListAdds(unittest.TestCase):
    def test_default_init(self):
        self.assertEqual([], dll().to_list())

    def test_collection_init(self):
        self.assertEqual([1, 2, 3], dll([1, 2, 3]).to_list())

    def test_push_back_on_empty(self):
        l = dll()
        l.push_back(1)
        self.assertEqual([1], l.to_list())

    def test_push_front_on_empty(self):
        l = dll()
        l.push_front(1)
        self.assertEqual([1], l.to_list())

    def test_push_front(self):
        l = dll([1, 2, 3])
        l.push_front(4)
        self.assertEqual([4, 1, 2, 3], l.to_list())

    def test_push_back(self):
        l = dll([1, 2, 3])
        l.push_back(4)
        self.assertEqual([1, 2, 3, 4], l.to_list())

    def test_insert_on_empty(self):
        l = dll()
        l.insert(1, 0)
        self.assertEqual([1], l.to_list())

    def test_insert(self):
        l = dll([1, 2, 3])
        l.insert(5, 1)
        self.assertEqual([1, 5, 2, 3], l.to_list())

    def test_insert_out_of_bounds(self):
        l = dll([1, 2, 3])
        with self.assertRaises(IndexError):
            l.insert(5, 10)
            l.insert(5, 3)
            l.insert(5, -1)


class TestDoubleLinkedListRemoves(unittest.TestCase):
    def test_pop_back_on_empty(self):
        l = dll()
        with self.assertRaises(IndexError):
            l.pop_back()

    def test_pop_front_on_empty(self):
        l = dll()
        with self.assertRaises(IndexError):
            l.pop_front()

    def test_pop_back(self):
        l = dll([1, 2, 3, 4])
        l.pop_back()
        self.assertEqual([1, 2, 3], l.to_list())

    def test_pop_front(self):
        l = dll([1, 2, 3, 4])
        l.pop_front()
        self.assertEqual([2, 3, 4], l.to_list())

    def test_clear_on_empty(self):
        l = dll()
        l.clear()
        self.assertEqual([], l.to_list())

    def test_clear(self):
        l = dll([1, 2, 3, 4])
        l.clear()
        self.assertEqual([], l.to_list())

    def test_delete_on_empty(self):
        l = dll()
        with self.assertRaises(ValueError):
            l.delete(1)

    def test_delete_existing_key(self):
        l = dll([1, 2, 3, 4, 5])
        l.delete(1)
        self.assertEqual([2, 3, 4 ,5], l.to_list())

    def test_delete_multiple_existing_keys(self):
        l = dll([1, 2, 1, 3])
        l.delete(1)
        self.assertEqual([2, 3], l.to_list())

    def test_delete_non_existing_key(self):
        l = dll([1, 2, 3, 4])
        with self.assertRaises(ValueError):
            l.delete("wow")


class TestAccessToElements(unittest.TestCase):
    def test_front_on_empty(self):
        l = dll()
        self.assertEqual(None, l.front())

    def test_front(self):
        l = dll([1, 2, 3])
        self.assertEqual(1, l.front())

    def test_back_on_empty(self):
        l = dll()
        self.assertEqual(None, l.back())

    def test_back(self):
        l = dll([1, 2, 3, 4])
        self.assertEqual(4, l.back())

    def test_get_item_on_empty(self):
        l = dll()
        with self.assertRaises(IndexError):
            l.get_item(1)

    def test_get_item(self):
        l = dll([1, 2, 3])
        self.assertEqual(1, l.get_item(0))

    def test_get_item_out_of_bounds(self):
        l = dll([1])
        with self.assertRaises(IndexError):
            l.get_item(10)
        with self.assertRaises(IndexError):
            l.get_item(-10)

    def test_contains(self):
        l = dll()
        self.assertEqual(False, l.contains(10))
        l = dll([1, 2, 3, 4])
        self.assertEqual(False, l.contains("hi"))
        self.assertEqual(True, l.contains(2))

    def test_size(self):
        l = dll()
        self.assertEqual(0, l.size())
        l = dll([1, 2, 3])
        self.assertEqual(3, l.size())
        l.clear()
        self.assertEqual(0, l.size())
        l.push_back(1)
        self.assertEqual(1, l.size())
        l.push_front(2)
        self.assertEqual(2, l.size())


if __name__ == '__main__':
    unittest.main()
