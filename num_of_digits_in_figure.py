# Counting digits in Figure

#from sympy import log
from math import log, floor

a = 145

x = floor(log(145, 10)) + 1
# log(145) with base of 10
# else: write
# log(145)/log(10)

print(x) # 3
