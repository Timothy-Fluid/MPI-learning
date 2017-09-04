import mpi4py.MPI as MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = None
if rank == 0:
    data = [1, 2, 3, 4]
    comm.send(data, dest=1, tag=11)
if rank == 1:
    print("On task " + str(rank) + " before recieve")
    print(data)
    data = comm.recv(source=0, tag=11)
    print("On task " + str(rank) + " after recieve")
    print(data)
