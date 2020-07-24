# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math

def primefactors(a):
	i = 2
	li = []
	while i * i <= a:
		if a % i == 0:
			li.append(i)
			a = a // i
		else:
			i = i + 1

	return li
		


def nthpowerfulnumber(n):
	s = 0
	z = 3
	if n == 0:
		return 1

	
	while s != n:
		z = z + 1
		l = primefactors(z)
		primes = list(set(l))
		print("--------------")
		print("s",s)
		print("z",z)
		print(primes)
		tem = 2
		for i in primes:
			if z % i != 0 or z % (i ** 2) != 0:
				tem = 1
			else:
				tem = 0	

		if tem == 0:
			s= s + 1
				

	return z