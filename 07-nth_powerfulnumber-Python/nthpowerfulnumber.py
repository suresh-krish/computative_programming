# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math

def primefactors(a):
	li = []
	while a % 2 == 0:
		li.append(2)
		a = a / 2

	for i in range(3,int(math.sqrt(a)) + 1,2):
		while a % i == 0:
			li.append(i)
			a = a / i

	return li
		


def nthpowerfulnumber(n):
	s = 0
	z = 3
	if n == 0:
		return 1

	
	while s != n:
		z = z + 1
		l = primefactors(z)
		print("z",z)
		print(l)
		for i in l:
			if z % i == 0 and z % (i * 2) == 0:
				s = s + 1
				break

	return z