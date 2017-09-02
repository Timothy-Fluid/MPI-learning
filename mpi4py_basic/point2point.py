import mpi4py.MPI as MPI

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()


if comm_rank == 0:
    data = 1
    comm.send(data,dest=1)
else:
    data = comm.recv(source=0)
    print('I receive a num : %d' % data)
