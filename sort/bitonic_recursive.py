import numpy as np


def bsort(begin, length, direction):
    # create a bitonic serie and sort it
    if length > 1:
        k = int(length / 2)
        bsort(begin, k, 'up')
        bsort(begin + k, k, 'down')

        bmerge(begin, length, direction)


def bmerge(begin, length, direction):
    # sort a bitonic serie
    if length > 1:
        k = int(length / 2)
        for i in range(begin, begin + k):
            if (direction == 'up' and array[i] > array[i + k])or (direction == 'down' and array[i] < array[i + k]):
                tmp = array[i]
                array[i] = array[i + k]
                array[i + k] = tmp  # This is a comparator
        bmerge(begin, k, direction)
        bmerge(begin + k, k, direction)


array = np.random.randint(0, 100, 32)

bsort(0, 32, 'up')
print(array)
