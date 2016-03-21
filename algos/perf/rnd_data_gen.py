import random
import time


class RandomDatasetGenerator(object):
    def __init__(self):
        self.random = random.Random(time.time())

    def get_sorted_list(self, size):
        """Complexity: O(n)"""
        ret_val = range(0, size)
        x = 0
        for i in ret_val:
            x = x + self.random.randint(1, 10)
            ret_val[i] = x
        return ret_val

    def get_unsorted_list(self, size):
        """Complexity: O(n)"""
        ret_val = self.get_sorted_list(size)
        self.random.shuffle(ret_val)
        return ret_val

    def get_existant_el(self, collection):
        """Complexity: O(1)"""
        return collection[self.random.randint(0, len(collection) - 1)]

    def get_non_existant_el_sorted(self, collection):
        """Complexity: O(1)"""
        while True:
            i = self.random.randint(0, len(collection) - 1)
            el = collection[i]
            new_el = el + self.random.randint(1, 10)
            if i == len(collection) - 1 or new_el < collection[i + 1]:
                return new_el

    def get_non_existant_el_unsorted(self, collection):
        """Complexity: O(nlogn)"""
        new_collection = collection[:]
        new_collection.sort()
        return self.get_non_existant_el_sorted(new_collection)
