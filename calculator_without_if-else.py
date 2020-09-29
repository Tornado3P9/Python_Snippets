# The following snippet shows how you can write a simple calculator without the need to use if-else conditions.

import operator
action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow
}
print(action['-'](50, 25)) # 25
