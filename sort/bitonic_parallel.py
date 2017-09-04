"""
This is the parallel implement of bitonic sort.
The number of processor must be power 2 (2^N).
Give the size of an array in each processor and 
give a sort direction. Random integers will be 
used as the initial data.
"""

import numpy as np
import mpi4py.MPI as MPI
import sys

# Main
# Initial the MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Initial the local array
localsize = int(sys.argv[1])
direction = sys.argv[2]
localarray = np.random.randint(0, localsize, localsize)
print("Before sort, Data in processor " + str(rank) + " :")
# print(localarray)

comm.Barrier()
begin = MPI.Wtime()
print(rank, ' begin', begin)
# sort the localarray
localarray = np.sort(localarray)

# bitonic sort

comm.Barrier()
end = MPI.Wtime()
print(rank, ' end ', end)
# if rank == 0:
print("Process " + str(rank) + "Time taken: " + str(end - begin) + ' s')

#print("After sort, Data in processor " + str(rank) + " :")
# print(localarray)


# def bitonic(direction):
#    global localarray
#
