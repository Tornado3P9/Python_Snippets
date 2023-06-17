## The following method can be used to merge two dictionaries.

# from Python 3.9 and later versions

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Version 1
merged_dict = dict1 | dict2

print(merged_dict)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4} dict1 and dict2 remain unchanged


# Version 2
dict1 |= dict2

print(dict1)    # {'a': 1, 'b': 2, 'c': 3, 'd': 4} dict1 has been changed



# before Python 3.9

def merge_two_dicts(a, b):
    c = a.copy()   # make a copy of a 
    c.update(b)    # modify keys and values of a with the ones from b
    return c


a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_two_dicts(a, b)) # {'y': 3, 'x': 1, 'z': 4}



## In Python 3.5 and above, you can also do it like the following:
def merge_dictionaries(a, b):
   return {**a, **b}

a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_dictionaries(a, b)) # {'y': 3, 'x': 1, 'z': 4}
