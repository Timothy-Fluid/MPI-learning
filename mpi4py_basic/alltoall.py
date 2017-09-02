import mpi4py.MPI as MPI
import numpy as np

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

data = comm.alltoall([comm_rank]*comm_size)
print(comm_rank,data)
