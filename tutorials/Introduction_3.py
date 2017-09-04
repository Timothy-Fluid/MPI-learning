import mpi4py.MPI as MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


if rank == 0:
    if size == 5:
        print("Success!")
    else:
        print("Error:This program must run")
        comm.Abort()
