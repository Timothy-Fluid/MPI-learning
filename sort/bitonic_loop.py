import numpy as np


def merge_up(begin, length):

    stage = int(np.log2(length))
    for j in range(stage):
        # begin compare each stage has 2^j comparator
        comparator = int(2**j)
        length_comparator = int(length / comparator)
        for i in range(begin, begin + length, length_comparator):
            # begin each comparator
            k = int(length_comparator / 2)
            for c in range(i, i + k):
                if array[c] > array[c + k]:
                    tmp = array[c]
                    array[c] = array[c + k]
                    array[c + k] = tmp
    return array


def merge_down(begin, length):

    stage = int(np.log2(length))
    for j in range(stage):
        # begin compare each stage has 2^j comparator
        comparator = int(2**j)
        length_comparator = int(length / comparator)
        for i in range(begin, begin + length, length_comparator):
            # begin each comparator
            k = int(length_comparator / 2)
            for c in range(i, i + k):
                if array[c] < array[c + k]:
                    tmp = array[c]
                    array[c] = array[c + k]
                    array[c + k] = tmp
    return array


# Test BM
print("Merge Method Test")
print("===================================")
array = np.array([3, 5, 8, 9, 10, 12, 14, 20, 95,
                  90, 60, 40, 35, 23, 18, 0], 'int64')
merge_up(0, 16)
print("Test Merge up,it should return a ascending serie")
print(array)
print("Bitonic Sort Test")
print("===================================")
N = 16
array = np.array([10, 20, 5, 9, 3, 8, 12, 14, 90, 0,
                  60, 40, 23, 35, 95, 18], 'int64')
print("Before Sorted ", array)
s = 2
while s < N:
    for i in range(0, N, 2 * s):
        merge_up(i, s)
        merge_down(i + s, s)
    s = s * 2

merge_up(0, N)
print("After Sorted", array)
