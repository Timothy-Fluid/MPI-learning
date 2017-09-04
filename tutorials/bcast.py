import mpi4py.MPI as MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

random_num = np.empty(1, 'float')

if rank == 0:
    random_num[0] = np.random.uniform(0)

comm.Bcast(random_num, root=0)
print("No." + str(rank) + " has the number: " + str(random_num[0]))
