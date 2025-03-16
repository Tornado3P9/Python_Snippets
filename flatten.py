# The following methods flatten a potentially deep list using recursion.

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


spread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]


def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs, list) else flat_list.append(xs)
    return flat_list


deep_flatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]


###################
# https://youtu.be/Ob8PUkdMlxE
# Memory efficiency:
from itertools import chain
from typing import Iterator

my_lists: list[list[int]] = [[1, 2, 3], [111, 222]]
my_chain: Iterator[int] = chain.from_iterable(my_lists)
print(list(my_chain))

from sys import getsizeof
from string import ascii_letters

iter1: Iterator[str] = iter(ascii_letters)
iter2: Iterator[int] = iter(range(1_000_000))
my_chain: Iterator[str | int] = chain(iter1, iter2)
print(getsizeof(iter1), 'bytes')
print(getsizeof(iter2), 'bytes')
print(getsizeof(my_chain), 'bytes')

extracted: list[str | int] = list(my_chain)
print(getsizeof(extracted), 'bytes')
