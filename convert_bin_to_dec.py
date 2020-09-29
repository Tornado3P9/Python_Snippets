# The following methods can be used to convert a binary number to decimal.


# bin(19) = 0b10011
# int('10010', 2) = 19


# >>> f'{0b1011010:#o}'
# '0o132'  # octal
#
# >>> f'{0b1011010:#x}'
# '0x5a'   # hexadecimal
#
# >>> f'{0b1011010:#0}'
# '90'     # decimal
#
# :#b -> converts to binary
# :#o -> converts to octal
# :#x -> converts to hexadecimal
# :#0 -> converts to decimal as above example


# def convBinToDec(binList):
#     binList = list(reversed(binList))
#     result = 0
#     for x in binList:
#         print(x)
#         result = result + x
#         result = result * 2
#     return result // 2


def convBinToDec(binList):
    binList = list(reversed(binList))
    result = 0
    while len(binList) > 0:
        result = result + binList.pop()
        result = result * 2
    return result // 2

convBinToDec([1,0,0,1,1])
