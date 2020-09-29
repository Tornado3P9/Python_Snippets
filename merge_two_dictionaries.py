# The following method can be used to merge two dictionaries.

def merge_two_dicts(a, b):
    c = a.copy()   # make a copy of a 
    c.update(b)    # modify keys and values of a with the ones from b
    return c


a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_two_dicts(a, b)) # {'y': 3, 'x': 1, 'z': 4}





## In Python 3.5 and above, you can also do it like the following:
#def merge_dictionaries(a, b):
#   return {**a, **b}
#
#
#a = { 'x': 1, 'y': 2}
#b = { 'y': 3, 'z': 4}
#print(merge_dictionaries(a, b)) # {'y': 3, 'x': 1, 'z': 4}
