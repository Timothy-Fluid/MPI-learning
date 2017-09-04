import mpi4py.MPI as MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

print("Hell World from process " + str(rank) + " rank " + str(size))
