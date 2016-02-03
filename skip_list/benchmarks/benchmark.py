from collections import namedtuple

from skip_list.skip_list import SkipList
import unittest
import time


def maximise(collection, array, m):
    sums_seen = collection()
    sums_seen.add(0)
    mod_running = 0
    best = 0
    for num in array:
        mod_running = (mod_running + num) % m
        sums_seen.add(mod_running)
        goal = (mod_running + 1) % m
        nearest_goal = sums_seen.ceiling(goal) or 0
        best = max(best, (mod_running - nearest_goal) % m)
    return best


class benchmark(object):
    def __init__(self,name):
        self.name = name
    def __enter__(self):
        self.start = time.time()
    def __exit__(self,ty,val,tb):
        end = time.time()
        print("%s : %0.3f seconds" % (self.name, end-self.start))
        return False

IMPLEMENTATIONS = [
    # SkipList,
]

TestData = namedtuple("TestData", ("mod_number", "data_array", "answer"))

def get_test_data(file_path):
    with open(file_path, "r") as test_file:
        num_cases = int(test_file.readline())
        test_data = []
        for _ in range(num_cases):
            size, mod = [int(x) for x in test_file.readline().split()]
            array = [int(x) for x in test_file.readline().split()]
            answer = int(test_file.readline())
            test_data.append(TestData(mod_number=mod,
                                      data_array=array,
                                      answer=answer))

    return test_data



DATA_FILES = [
    # "skip_list/benchmarks/large_input.txt",
    "skip_list/benchmarks/medium_input_converted.txt"
    # "skip_list/benchmarks/small_input.txt"
]

if __name__ == "__main__":
    for data_file in DATA_FILES:
        test_data = get_test_data(data_file)
        for test in test_data:
            expected = test.answer
            for implementation in IMPLEMENTATIONS:
                # with benchmark(implementation):
                actual  = maximise(implementation, test.data_array, test.mod_number)
                if expected != actual:
                    print(("Wrong answer.  Expected {expected}, "
                           "but got {actual}, difference of {difference} on {data}...").format(
                               expected=expected,
                               actual=actual,
                               difference=expected - actual,
                               data=test.data_array[:5]))
