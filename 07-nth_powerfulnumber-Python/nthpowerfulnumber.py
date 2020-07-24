# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def primefactors(a):
	li = []
	p = []
	for i in range(2,a + 1):
		flag = 0
		for j in range(2,i):
			if i % j == 0:
				break
		if flag == 0:
			li.append(i)
	for i in li:
		if p % i == 0:
			p.append(i)

	return p
		


def nthpowerfulnumber(n):
	s = 0
	while s != n:
		l = primefactors(n)
		for i in l:
			if n % i == 0 and n % (i * 2) == 0:
				s = s + 1

	return i