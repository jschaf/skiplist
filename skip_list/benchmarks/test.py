from skip_list.tests.test_skip_list import SkipListTestMixin
from .zhukov_skip_list import Skiplist as ZhukovSkipList
import unittest

class TestZhukovSkipList(SkipListTestMixin, unittest.TestCase):
    SkipListClass = ZhukovSkipList

if __name__ == "__main__":
    unittest.main()

