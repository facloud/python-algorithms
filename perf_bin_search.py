import random
import bin_search


class PerfBinSearch(object):
    def get_random_sorted_list(self, size):
        ret_val = []

        last_val = 0
        add_idx = 0
        add_range = range(0, 10)
        for i in xrange(size):
            add_idx += 1
            add = add_range[add_idx % 10]

            last_val += add
            ret_val.append(last_val)

        return ret_val

    def run(self, sample):
        (collection, element) = sample
        return bin_search.contains(collection, element)


class PerfBinSearchFound(PerfBinSearch):
    def get_random_input(self, size):
        l = self.get_random_sorted_list(size)
        element_idx = random.randint(0, size-1)
        return (l, l[element_idx])

    def validate_result(self, sample, result):
        return result is True


class PerfBinSearchNotFound(PerfBinSearch):
    def get_random_input(self, size):
        l = self.get_random_sorted_list(size)

        while True:
            el_idx = random.randint(0, size-2)
            el = l[el_idx]
            next_el = l[el_idx + 1]
            if next_el > el + 1:
                return (l, el + 1)

        raise Exception('cannot reach this point')

    def validate_result(self, sample, result):
        return result is False
