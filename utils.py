import re


def get_key_by_value(dictionary, val):
    for key, value in dictionary.items():
        if value == val:
            return key
    return None


def get_keys_by_value(dictionary, lst):
    return [get_key_by_value(dictionary, val) for val in lst]


def manhattan_distance(point1, point2):
    return sum(abs(a - b) for a, b in zip(point1, point2))


def replace_or_append(lst, index, value):
    if index is None:
        lst.append(value)
    else:
        lst[index] = value


def pairwise(lst):
    return zip(lst[::2], lst[1::2])


def neighbours(lst):
    return zip(lst, lst[1:])


def get_digits(line):
    return [int(x) for x in re.findall(r'\d+', line)]


def list_reductions(lst):
    """
    Generate sublists by removing one element at a time from the input list.
    @param lst: The input list.
    @return: A list of sublists, each with one element removed from the original list.
    """
    return [lst[:i] + lst[i + 1:] for i in range(len(lst))]

def slice_lists(lst, slices):
    length = len(lst)
    if length == 1:
        return lst
    else:
        return [(lst[i * (length // slices): (i + 1) * (length // slices)]) for i in range(slices)]