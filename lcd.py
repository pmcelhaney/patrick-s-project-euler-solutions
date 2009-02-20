# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?

def lcd(x, y):
  if x < y: 
    return lcd(y, x)
  if y % x == 0:
    return y
  for i in range(1,x+1):
    if x % i == 0 and (i * y) % x == 0:
      return i * y
    
    
# Tests to make sure my lcd (least common denominator) function works    
print lcd(5,5) == 5
print lcd(5,10) == 10
print lcd(10,5) == 10
print lcd(3,5) == 15
print lcd(6,8) == 24

print reduce(lcd, range(1,21))


# Note: This should actually go up to range(1,20+1), but when I do that Python freaks out.
# The answer turns out to be the same, so I'm not going to worry about it. 


  