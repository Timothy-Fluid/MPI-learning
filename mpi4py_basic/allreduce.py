import mpi4py.MPI as MPI

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

data = comm.allreduce(comm_rank,op=MPI.PROD)
print(comm_rank,data)
