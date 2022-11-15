import sys

# for eachArg in sys.argv:
#     print(eachArg)

num = int(sys.argv[1])

list = []
i = 1
while i < num:
    if num % i != 0: # '==' Divisor, '!=' non-divisive
        list.append(i)
    i += 1
print(list)
