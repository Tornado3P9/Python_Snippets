# This snippet shows that you can use enumerate to get both the values and the indexes of lists.

list = ["a", "b", "c", "d"]
for index, element in enumerate(list): 
    print("Value", element, "Index ", index, )
# ('Value', 'a', 'Index ', 0)
# ('Value', 'b', 'Index ', 1)
#('Value', 'c', 'Index ', 2)
# ('Value', 'd', 'Index ', 3)
