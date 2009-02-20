    
def threes_and_fives(max):
  for x in range(1,max):
    if x % 3 == 0 or x % 5 == 0:
      yield x
      
  


print reduce(lambda x, y: x+y, threes_and_fives(1000))
    
    
    
