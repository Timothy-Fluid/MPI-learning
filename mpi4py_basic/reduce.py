#!/usr/bin/env python
import mpi4py.MPI as MPI

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

k = (1.0 if comm_rank % 2 == 0 else -1.0) / (2*comm_rank + 1)
data = comm.reduce(k, root=0,op=MPI.SUM)
if comm_rank == 0:
    pi = data*4
    print(pi)

