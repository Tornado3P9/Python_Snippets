# The following methods show just another way of handling the problems.

#Version-2 using a list
def fib(number):
    a,b, = 1,1
    lst = []
    for i in range(number):
        temp = a
        a = b
        b = temp + b
        lst.append(temp)
    return lst

print(fib(12))

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

print(isprime(7))

from math import log
def primepi(num):
    n = num
    return n / log(n) # estimate number of primes until 'x'

print(primepi(10**14))

def prime(num):
    n = num
    return n * log(n) # estimate the 'x'th prime number

print(prime(500))

def ggt(a,b):
    while a != b:
        if b > a:
            a,b = b,a
        a = a - b
    return a

print(ggt(12,36))

from math import gcd

print(gcd(12,36))

def kgV(a,b):
    m = 1 #multiplier
    while True:
        if (result := m * a) % b == 0:
            break
        m += 1
    return result

print(kgV(4,9)) #https://docs.python.org/3/whatsnew/3.8.html#new-features

from math import lcm #Erst ab python3.9

print(lcm(4,9))
