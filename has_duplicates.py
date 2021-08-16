## Version A: Return Boolean!
# The following method checks whether a list has duplicate values by using the fact that set()
# contains only unique elements.
x = [1,2,3,4,5,5]
y = [1,2,3,4,5]

def has_duplicates(lst):
    return len(lst) != len(set(lst))

has_duplicates(x) # True
has_duplicates(y) # False



## Version B: Show the duplicates!
some_list = ['a','b','c','b','d','m','n','n']

def show_duplicates(lst):
    duplicates = []
    for value in lst:
        if lst.count(value) > 1:
            if value not in duplicates:
                duplicates.append(value)
    return duplicates

print(show_duplicates(some_list)) # ['b', 'n']
