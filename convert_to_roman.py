#     list = list[::-1]  # list.reverse()
#
#     # Print List Items in Single Row
#     for i in list:
#         print(i, end="")

romanDict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500,"CM": 900, "M": 1000}


def convert2roman(input_number):
    output = None
    for symbol, integer in romanDict.items():
        if integer == input_number: return symbol
        if input_number > integer:
            output = symbol

    remaining = input_number - romanDict[output]
    return output + convert2roman(remaining)


def main():
    print('Geben Sie ein ganze Zahl zwischen 1 und 3999 ein:')
    x = int(input())
    if 1 <= x <= 3999:
        print(convert2roman(x))
    else:
        print('Sorry, wrong input!')


if __name__ == '__main__':
    main()
