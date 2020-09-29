# The following method can be used to convert a decimal number to binary.

def convDecToBin(number):
    h = []
    while number > 0:
        h.append(number%2)
        number = number // 2
    return list(reversed(h))

convDecToBin(42) # [1,0,1,0,1,0]


# The following method can be used to convert a decimal number to hex.

def convDecToHex(number):
    i = []
    while number > 0:
        i.append(number%16)
        number = number // 16
    return list(reversed(i))

convDecToHex(32) # [2,0]


# The following methods can be used to convert a binary number to decimal.

def convBinToDec1(binList):
    binList = list(reversed(binList))
    result = 0
    while len(binList) > 0:
        result = result + binList.pop()
        result = result * 2
    return result // 2

convBinToDec1([1,0,0,1,1]) # 19


bin(19) # 0b10011
oct(19) # 0o23
hex(19) # 0x13
int('10010', 2) # 19

# octal
f'{0b1011010:#o}' # '0o132'
# hexadecimal
f'{0b1011010:#x}' # '0x5a'
# decimal
f'{0b1011010:#0}' # '90'
# :#b -> converts to binary
# :#o -> converts to octal
# :#x -> converts to hexadecimal
# :#0 -> converts to decimal as above example
