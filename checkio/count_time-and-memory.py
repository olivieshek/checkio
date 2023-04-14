# Import
import random
import timeit
from guppy import hpy

# Main Function
def main():
    n = random.randrange(10, 20)
    data = [0] * n
    for i in range(n):
        data[i] = random.randrange(10)

# Count Time Used
start_time = timeit.default_timer()
main()
print(f'Time: {(timeit.default_timer() - start_time)} sec')

# Count Memory Used
h = hpy()
print(f'Memory: {round(h.heap().size * 0.000001, 3)} MB')