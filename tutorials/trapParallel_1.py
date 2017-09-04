import numpy as np
import sys
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

# Initialize the MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# command line input
a = float(sys.argv[1])
b = float(sys.argv[2])
n = int(sys.argv[3])


def f(x):
    return x**2


def integrate(a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    x_i = np.linspace(a, b, n + 1)
    for x in x_i[1:n]:
        integral = integral + f(x)
    return integral * h


# local information
h = (b - a) / n
local_size = int(n / size)
local_start = a + rank * local_size * h
local_end = local_start + local_size * h

begin = MPI.Wtime()

# initial the variable in each processor
integral = np.zeros(1)
recv_buffer = np.zeros(1)

integral[0] = integrate(local_start, local_end, local_size)
#print("PROC " + str(rank) + " " + str(integral[0]))

if rank == 0:
    total = integral[0]
    for i in range(1, size):
        comm.Recv(recv_buffer, source=i, tag=i)
        total += recv_buffer[0]
else:
    comm.Send(integral, dest=0, tag=rank)

# ROOT SHOWING THE RESULT
if rank == 0:
    end = MPI.Wtime()
    print("With n = " + str(n) + "trapezoids, the estimate of the integral from a = " +
          str(a) + " b = " + str(b) + " is " + str(total))
    print("Time taken " + str(end - begin))
