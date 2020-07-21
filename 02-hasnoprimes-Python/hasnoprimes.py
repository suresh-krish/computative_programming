# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def isPrime(a):
	for i in range(2,a):
		if a % i == 0:
			return 1
	return 0


def fun_hasnoprimes(l):
	flag = 0
	for i in l:
		for j in i:
			a = isPrime(j)
			if a == 0:
				return False

	return True


