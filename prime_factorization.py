import sys

# Example:
# python3 prime_factorization.py 42
# --> [2, 3, 7]

n = int(sys.argv[1])

# Prime factorization
def primefactors(n):
    result = []
    i = 2
    while i <= n:
        while n % i == 0:
            result.append(i)
            n = n / i
        i = i + 1
    return result

print(primefactors(n))
