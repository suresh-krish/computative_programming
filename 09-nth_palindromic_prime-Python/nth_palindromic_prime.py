# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2
import math

def is_prime(p):
	flag = 0
	for i in range(2,p):
		if p%i == 0:
			flag = 1
	if flag == 0:
	    return 0


def fun_nth_palindromic_prime(n):
	if n == 0:
		return 2

	else:
		a = 0
		p = 3
		if n == 0:
			return 2

		while a < n:
			k = is_prime(p)
			if k == 0:
				ch = str(p)
				if ch == ch[::-1]:
					a = a + 1
				p = p + 1
			else:
				p = p + 1
		return p - 1