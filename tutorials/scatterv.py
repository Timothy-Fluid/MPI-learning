import numpy as np
import mpi4py.MPI as MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    x = np.linspace(0, 100, 11)
else:
    x = None

# local
if rank == 2:
    x_local = np.zeros(9)
else:
    x_local = np.zeros(1)

# scatter
if rank == 0:
    print("Scatter")

comm.Scatterv([x, (1, 1, 9), (0, 1, 2), MPI.DOUBLE], x_local, root=0)
print("Procs " + str(rank) + " has " + str(x_local))

comm.Barrier

# Gather
if rank == 0:
    xgathered = np.zeros(11)
else:
    xgathered = None

comm.Gatherv(x_local, [xgathered, (1, 1, 9), (0, 1, 2), MPI.DOUBLE])
print("Procs " + str(rank) + " has " + str(xgathered))
