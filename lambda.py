# https://youtu.be/K36DX1hYoow

from typing import Callable, Iterator
from itertools import starmap


mapped: Iterator[str] = map(lambda n: n * 'X', [1, 2, 3, 4])
print(list(mapped))


display_list: Callable[[list], None] = lambda l: print(*l, sep=', ', end='.\n')
display_list(['Bob', 'James', 'Guy'])
display_list(['1', '2', '3'])


data: list[tuple[str, int]] = [('Bob', 3), ('X', 5), ('Python', 2)]
sm: Iterator[str] = starmap(lambda s, n: s * n, data)
print(list(sm))
