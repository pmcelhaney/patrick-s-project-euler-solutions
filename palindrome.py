# -*- coding: utf-8 -*-
#
# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#	
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
	s = str(n)
	return s == s[::-1]
	


def largest_palindrome(min, max):
	largest = 0
	parts = (0, 0)
	for x in xrange(min,max+1):
		for y in xrange(min,x+1):
			n = x * y
			if n > largest and is_palindrome(n):
				largest = n
				parts = (x, y)
	return parts, largest
	

print largest_palindrome(100, 999)
		
