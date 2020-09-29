# This method chunks a list into smaller lists of a specified size.

def chunk(list, size):
    return [list[i:i+size] for i in range(0,len(list), size)]
