import mpi4py.MPI as MPI

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

print("Hello World! I'm the %d process of %d process "%(comm_rank,comm_size))
