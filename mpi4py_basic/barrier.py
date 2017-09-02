import mpi4py.MPI as MPI
import sys


comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

print(comm_rank,'begin')
sys.stdout.flush()
comm.barrier()
print(comm_rank,'end')
