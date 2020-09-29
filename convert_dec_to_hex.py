# The following method can be used to convert a decimal number to hex.

def convDecToHex(n):
    i = []
    while n > 0:
        i.append(n%16)
        n = n // 16
    return list(reversed(i))

convDecToHex(32)
#[2,0]
