import numpy as np


class Sort():
    ''' 
    An attmpt to design a class to generate a random integer
    array and sort the array in different ways
    Now the sort method include:
       1.    Bitonic
    '''

    def __init__(self, n):
        self.array = np.random.randint(0, 1000, n)
        self.length = n

    def Bitonic(self, direction):
        # Bitonic sort
        begin = 0
        length = self.length
        '''
        direction    Meaning
        True         Ascending sort
        False        Descending sort
        '''
        if direction == 'up':
            direction = True
        elif direction == 'down':
            direction = False
        # Call the bitonic sort function
        self.Bitonic_Sort(begin, length, direction)

    def Bitonic_Sort(self, begin, length, direction):
        # recursive function to sort the bitonic series
        if length > 1:
            # divide the series in two parts
            # Sort each one
            k = int(length / 2)
            self.Bitonic_Sort(begin, k, True)
            self.Bitonic_Sort(begin + k, k, False)
            self.Bitonic_Merge(begin, length, direction)

    def Bitonic_Merge(self, begin, length, direction):
        # sort the bitonic series
        if length > 1:
            k = int(length / 2)
            for i in range(begin, begin + k):
                if direction == (self.array[i] > self.array[i + k]):
                    self.swap(i, i + k)
            self.Bitonic_Merge(begin, k, direction)
            self.Bitonic_Merge(begin + k, k, direction)

    def swap(self, i, j):
        # change the location a element i and j
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp


#test_array = Sort(32)
#tmp = test_array.array.copy()
#print('Befort sort: ' + str(test_array.array))
# test_array.Bitonic('up')
#print('After sort: ' + str(test_array.array))
