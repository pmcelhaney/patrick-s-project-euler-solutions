# coding: UTF-8
#
# Starting in the top left corner of a 2×2 grid, there are 6 routes (without
# backtracking) to the bottom right corner.
#  
# How many routes are there through a 20×20 grid?


cache = {(0,0) : 1}

def count_paths(x,y):
    global cache
    
    if x == 0 or y == 0:
        return 1
    
    if (x,y) in cache:
        return cache[(x,y)]
        
    paths = count_paths(x-1, y) + count_paths(x, y-1) 
    
    cache[(x,y)] = paths
    cache[(y,x)] = paths
    
    return paths
    
print count_paths(20,20) 

