#!/usr/bin/env python
import mpi4py.MPI as MPI

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

data = comm.allgather(comm_rank)
print(data)


