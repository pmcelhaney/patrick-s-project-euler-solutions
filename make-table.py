# ProjectEuler.net is down, but I remember the problem.  
# It involved a 10x10 (I think) table of random two digit numbers.
# I'm generating my own table, and I'll solve the problem with my own data.
# Once the site is back up I should be able to plug in the real data and get the answer.

import random

for x in xrange(0,10):
    row = ["%02d" % random.randrange(0,100) for y in xrange(0,10)]
    print " ".join(row) 