import mpi4py.MPI as MPI

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

if comm_rank == 0:
    data = [1,2,3]
else:
    data = None

data = comm.scatter(data,root=0)
print("Process %d receive "%comm_rank,data)
