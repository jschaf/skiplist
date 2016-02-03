"""test_maximise.py - test Skip List set implementations against the Hacker
Rank maximise sum problem.

This is a short test to ensure the code passes before we subject it to the
ridiculously sized data.
"""
from .benchmark import maximise


class TestMaximiseMixin(object):
    def test_single(self):
        self.assertEqual(self.maximise_fn([1], 2), 1)

    def test_single_overflow(self):
        self.assertEqual(self.maximise_fn([3], 2), 1)

    def test_example(self):
        self.assertEqual(self.maximise_fn([3, 3, 9, 9, 5], 7), 6)

    def test_zeroes(self):
        self.assertEqual(self.maximise_fn([0, 0, 0], 1), 0)
        self.assertEqual(self.maximise_fn([0, 0, 0], 3), 0)

    def test_ones(self):
        self.assertEqual(self.maximise_fn([1, 1, 1, 1], 1), 0)
        self.assertEqual(self.maximise_fn([1, 1, 1, 1], 2), 1)
        self.assertEqual(self.maximise_fn([1, 1, 1, 1], 3), 2)
        self.assertEqual(self.maximise_fn([1, 1, 1, 1], 4), 3)

    def test_simple(self):
        self.assertEqual(self.maximise_fn([5, 4], 7), 5)
        self.assertEqual(self.maximise_fn([3, 1, 2], 7), 6)
        self.assertEqual(self.maximise_fn([1, 1, 8], 7), 3)


# class TestMaximise(TestMaximiseMixin, unittest.TestCase):
#     maximise_fn = lambda self, array, m: maximise(SkipList, array, m)


# if __name__ == "__main__":
#     unittest.main()
