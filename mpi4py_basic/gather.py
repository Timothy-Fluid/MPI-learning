#!/usr/bin/env python
import mpi4py.MPI as MPI

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

if comm_rank == 0:
    data = comm.gather(comm_rank,root=0)
    print(data)
else:
    comm.gather(comm_rank,root=0)

