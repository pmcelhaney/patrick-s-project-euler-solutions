def prod( *aList ):
    p= 1
    for n in aList:
        p *= n
    return p
    
print prod([3,4,5])
