import types
from Decorator import logger

@logger
def flat_generator(list_of_lists):
    i = 0
    j = 0
    while i < len(list_of_lists):
        while j < len(list_of_lists[i]):
            item = list_of_lists[i][j]
            j += 1
            yield item
        j = 0
        i += 1

test_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

flat_generator(test_list)