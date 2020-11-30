# This snippet shows four different ways for printing a float number
# with a specified number of decimal places


# One way:

number = 1
'{:.2f}'.format(number) #1.00
'{:.3f}'.format(number) #1.000

# second way:

'%.2f' % number #1.00
'%.3f' % number #1.000

# third way:

format(number, ".2f") #1.00
format(number, ".3f") #1.000

# forth way:

round(result, 2) #1.00
round(result, 3) #1.000
