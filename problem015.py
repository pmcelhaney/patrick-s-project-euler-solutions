# coding: UTF-8
#
# Starting in the top left corner of a 2×2 grid, there are 6 routes (without
# backtracking) to the bottom right corner.
#  
# How many routes are there through a 20×20 grid?


cache = {(0,0) : 0}

def count_paths(x,y):
    global cache
    
    if (x,y) in cache:
        return cache[(x,y)]
    
    if (y,x) in cache:
        return cache[(y,x)]
     
    paths = 0
    
    if x > 0:
        paths = paths + count_paths(x-1, y)
    if y > 0: 
        paths = paths + count_paths(x, y-1)
         
    cache[(x,y)] = paths
    
    return paths
    
print count_paths(20,20) 