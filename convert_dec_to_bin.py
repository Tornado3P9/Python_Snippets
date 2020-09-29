# The following method can be used to convert a decimal number to binary.

def convDecToBin(number):
    h = []
    while number > 0:
        h.append(number%2)
        number = number // 2
    return list(reversed(h))

convDecToBin(42);
