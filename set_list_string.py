l = [1,2,3]

set(l)       # {1, 2, 3}
list(set(l)) # [1, 2, 3] but the order is not fixed
str(l)       # '[1, 2, 3]'


string = "name"

list(string) # ['n', 'a', 'm', 'e']
set(string) # {'a', 'm', 'n', 'e'}

charlist = ['n', 'a', 'm', 'e']
for i in charlist:
    print(i, end ="") # name
