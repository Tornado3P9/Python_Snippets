# The following method gives back the first 'x' numbers in the fibonacci sequence.

def fib(number):
    a,b = 0,1
    for i in range(number):
        yield a
        a, b = b, a+b


for n,x in enumerate(fib(20)):
    print(n+1, x)
