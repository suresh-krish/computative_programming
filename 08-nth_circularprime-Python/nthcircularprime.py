# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).


def isprime(num):
	c = 0
	for i in range(1,num+1):
		c= c+1
	return(c==2)
def checkCircular(N) :
	if("0" in str(N)):
		return False
	leng = len(str(n))
	if(leng == 1):
		if(isprime(N)):
			return True
		return False
	i = 0
	rem = 0
	while(i<leng):
		rem = N%10
		N = N//10
		N = rem *(10 **(leng -1)) + N
		if not isprime(N):
			return False
		i = i+1
	return True

def nthcircularprime(n):
# 	# Your code goes here
	l = [2,3,5,7]
	start = 1
	k =0
	while(True):
		if(len(str(start))== 1 and start in l):
			if(k == n):
				return start
			else:
				k = k + 1
		else:
			if(checkCircular(start) == True):
				if(k == n):
					return start
				else:
					k = k + 1
