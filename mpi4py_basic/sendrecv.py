import mpi4py.MPI as MPI
import numpy as np

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()


if comm_rank == 0:
    data = [1,2,3]
    data = comm.sendrecv(data,dest=1)
    print(data)
else:
    data = comm.recv(source=0)
    data = [x*2 for x in data]
    comm.send(data,dest=0)
