import unittest

def maximise(collection, array, m):
    sums_seen = collection
    sums_seen.add(0)
    mod_running = 0
    best = 0
    for num in array:
        mod_running = (mod_running + num) % m
        sums_seen.insert(mod_running)
        goal = (mod_running + 1) % m
        nearest_goal = sums_seen.ceiling(goal)
        best = max(best, (mod_running - nearest_goal) % m)
    return best

def main(file):
    for _ in range(num_cases):
        size, mod = [int(x) for x in file.readline().split()]
        array = [int(x) for x in file.readline().split()]
        print(maximise(array, mod))

class TestMaximise(unittest.TestCase):

    def test_single(self):
        self.assertEqual(maximise([1], 2), 1)


    def test_single_overflow(self):
        self.assertEqual(maximise([3], 2), 1)


    def test_example(self):
        self.assertEqual(maximise([3, 3, 9, 9, 5], 7), 6)


    def test_zeroes(self):
        self.assertEqual(maximise([0, 0, 0], 1), 0)
        self.assertEqual(maximise([0, 0, 0], 3), 0)


    def test_ones(self):
        self.assertEqual(maximise([1, 1, 1, 1], 1), 0)
        self.assertEqual(maximise([1, 1, 1, 1], 2), 1)
        self.assertEqual(maximise([1, 1, 1, 1], 3), 2)
        self.assertEqual(maximise([1, 1, 1, 1], 4), 3)

    def test_simple(self):
        self.assertEqual(maximise([5, 4], 7), 5)
        self.assertEqual(maximise([3, 1, 2], 7), 6)
        self.assertEqual(maximise([1, 1, 8], 7), 3)


class TestSkipList(unittest.TestCase):

    pass
