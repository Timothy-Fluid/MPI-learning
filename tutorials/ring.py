import mpi4py.MPI as MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

toy = np.empty(1)

if rank != 0:
    comm.Recv(toy, source=rank - 1, tag=0)
    print("Procs " + str(rank) + " receive " +
          str(toy) + " from Procs" + str(rank - 1))
else:
    toy[0] = 1.

comm.Send(toy, dest=(rank + 1) % size, tag=0)

if rank == 0:
    comm.Recv(toy, source=size - 1, tag=0)
    print("Procs " + str(rank) + " receive " +
          str(toy) + " from Procs" + str(size - 1))
