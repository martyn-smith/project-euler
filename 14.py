# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 15:27:02 2014

@author: c1346299
"""

def Euler_14():
	#verified
	#to add: caching
	max_iterations = 0
	big_n = 0
	for n in range(1, int(1e+6)):
		iterations = collatz_sequence(n)
		if iterations > max_iterations:
			max_iterations = iterations
			big_n = n
	return big_n
	
def collatz(n):
	if (n % 2 == 0):
		n /= 2
	else:
		n *= 3
		n += 1
	return n
	
def collatz_sequence(n):
	iterations = 0
	while (n > 1):
		iterations += 1
		n = collatz(n)
	return iterations
	
print Euler_14()