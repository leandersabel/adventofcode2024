def get_key_by_value(dictionary, val):
    for key, value in dictionary.items():
        if value == val:
            return key
    return None


def get_keys_by_value(dictionary, list):
    return [get_key_by_value(dictionary, val) for val in list]


def manhattan_distance(point1, point2):
    return sum(abs(a - b) for a, b in zip(point1, point2))


def replace_or_append(lst, index, value):
    if index is None:
        lst.append(value)
    else:
        lst[index] = value


def pairwise(lst):
    return zip(lst[::2], lst[1::2])
