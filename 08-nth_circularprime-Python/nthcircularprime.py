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
def nthcircularprime(n):
	# Your code goes here
	l = [2,3,5,7]
	start = 1
	k =0
	while(True):
		flag = False
		if(len(str(start))== 1 and start in l):
			if(k == n):
				return start
			else:
				k = k + 1
		else:
			if(isprime(start) == True and isprime(int(str(start)[::-1])) == True):
				s = str(start)
				for i in range(0,len(s)-1):
					Lfi= s[0 : 1]
					Lse = s[1 :]
					s = Lse+Lfi
					if(isprime(int(s)) == False):
						flag = True
						break
				if(flag == False):
					if(k == n):
						return start
					else:
						k = k + 1