import numpy as np
import mpi4py.MPI as MPI
import sys

# Initialize
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = int(sys.argv[1])
x = np.linspace(0, 10, n) if rank == 0 else None
y = np.linspace(0, 10, n) if rank == 0 else None

# The communication can only deliver numpy.array kind
# data
dot = np.array([0.])
local_n = np.array([0])
# check if n is divided by number of procs
if rank == 0:
    if n != y.size:
        print("Dimension mismatch")
        comm.Abort()
    elif n % size != 0:
        print("n must be divided by number of procs")
        comm.Abort()
    else:
        local_n[0] = n / size

# pass the local size to other process
comm.Bcast(local_n, root=0)

print(local_n)
x_local = np.zeros(local_n[0])
y_local = np.zeros(local_n[0])

# send each part of the vector to each procs
comm.Scatter(x, x_local, root=0)
comm.Scatter(y, y_local, root=0)

# initial local dot product
local_dot = np.array([np.dot(x_local, y_local)])

# reduce the sum
comm.Reduce(local_dot, dot, op=MPI.SUM, root=0)

# Print at master procs
if rank == 0:
    print("Serial dot product " + str(np.dot(x, y)))
    print("Parallel dot product " + str(dot[0]))
