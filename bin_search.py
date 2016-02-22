def contains(collection, element):
    return element in collection


def _bs_locate(ordered, element):
    low = 0
    high = len(ordered)-1
    while high >= low:
        mid = (low+high)/2
        if ordered[mid] == element:
            return mid
        elif ordered[mid] < element:
            low = mid+1
        else:
            high = mid-1
    return -(low+1)


def bs_contains(ordered, element):
    idx = _bs_locate(ordered, element)
    return idx >= 0


def bs_insert(ordered, element):
    idx = _bs_locate(ordered, element)
    if idx >= 0:
        return ordered

    idx = -(idx+1)
    ordered.insert(idx, element)
    return ordered
