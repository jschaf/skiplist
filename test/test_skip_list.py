import unittest

from skip_list.skip_list import SkipList

class TestSkipList(unittest.TestCase):

    def test_empty(self):
        "Test operations on an empty skip list."
        skip = SkipList()
        self.assertIsNone(skip.ceiling(9))
        self.assertIsNone(skip.ceiling(None))


    def test_order_empty(self):
        skip = SkipList()
        self.assertEqual(list(skip), [])


    def test_ceiling_one_elem(self):
        "Test operations on a skip list with one element."
        skip = SkipList()
        skip.add(1)
        self.assertEqual(skip.ceiling(-1), 1)
        self.assertEqual(skip.ceiling(0), 1)
        self.assertEqual(skip.ceiling(1), 1)
        self.assertIsNone(skip.ceiling(2))


    def test_order_one_elem(self):
        skip = SkipList()
        skip.add(2)
        self.assertEqual(list(skip), [2])


    def test_ceiling_two_elems(self):
        "Test operations on a skip list with two elements."
        skip = SkipList()
        skip.add(1)
        skip.add(10)
        self.assertEqual(skip.ceiling(-1), 1)
        self.assertEqual(skip.ceiling(0), 1)
        self.assertEqual(skip.ceiling(1), 1)
        self.assertEqual(skip.ceiling(2), 10)
        self.assertEqual(skip.ceiling(7), 10)
        self.assertEqual(skip.ceiling(10), 10)

        self.assertIsNone(skip.ceiling(11))
        self.assertIsNone(skip.ceiling(12))


    def test_order_two_elems(self):
        skip = SkipList()
        skip.add(2)
        skip.add(4)
        self.assertEqual(list(skip), [2, 4])

        # reverse order
        skip = SkipList()
        skip.add(4)
        skip.add(2)
        self.assertEqual(list(skip), [2, 4])
