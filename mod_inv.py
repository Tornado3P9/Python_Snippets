import sys

x = int(sys.argv[1])
n = 26

y = pow(x, -1, mod=n)

print(f"\n{x}^-1 mod {n} = {y}")
print(f"{y} * {x} % {n} == 1  ->  {y * x % n == 1}\n")