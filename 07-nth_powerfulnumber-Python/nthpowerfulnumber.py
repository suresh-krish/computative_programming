# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math

def nthpowerfulnumber(n):
	s = 0
	z = 3
	if n == 0:
		return 1

	
	while s != n:
		z = z + 1
		while z % 2 == 0:
			po = 0
			while z % 2 == 0:
				z = z // 2
				po = po + 1

			if po == 1:
				z = z + 1
				break
			else:
				s = s + 1
		
		for i in range(3,int(math.sqrt(z))+1,2):
			po = 0
			while (z % i == 0):
				z = z // i
				po = po + 1

			if po == 1:
				z = z + 1
				break
			else:
				s = s + 1

	return z