#!/usr/bin/env python
import mpi4py.MPI as MPI

# Initialize
comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()
print("MPI task" + str(comm_rank) + "has started...")
array_size = 16000000
domain_size = int(array_size / comm_size)
tag1 = 1
tag2 = 2

# For master task
if comm_rank == 0:
