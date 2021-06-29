# This snippet shows different ways to round numbers

from math import floor, ceil

# floor()
print(floor(-23.11)) # =>  -24.0
print(floor(300.16)) # =>  300.0
print(floor(300.72)) # =>  300.0

# ceil()
print(ceil(-23.11))  # =>  -23.0
print(ceil(300.16))  # =>  301.0
print(ceil(300.72))  # =>  301.0

# round()
print(round(51.6))           # =>   52
print(round(80.23456, 2)     # =>   80.23
print(round(100.000056, 3)   # =>  100.0
print(round(-100.000056, 3)  # =>  100.0
