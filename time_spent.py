# This snippet can be used to calculate the time it takes to execute a particular code.

import time

start_time = time.time()

a = 1
b = 2
c = a + b
print(c) #3

end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)

# ('Time: ', 1.1205673217773438e-05)

#####################################################################################
# Jupyter Notebook
import math
f = lambda x, y: 3*x**2 + math.log(x**2 + y**2 + 1)
f(17, 42) # 874.6275443904885

%timeit f(17, 42) # 1.59 µs ± 46 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
