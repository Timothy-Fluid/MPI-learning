import mpi4py.MPI as MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank % 2 != 0:
    print("Hello World from process " + str(rank) + "out of " + str(size))
else:
    print("Goodbye from process " + str(rank))
