# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)


def fun_nth_happy_number(n):
	if n == 0:
		return 1
	else :
		l = []
		nth = 0
		p = 2
		s = 2
		while True:
			if p!=0:
				sum = 0
				q = p%10
				sum = sum + q * q
				p = p // 10
			elif sum == 1 or sum == 4:
				nth = nth + 1
				
				if nth == n:
					break
				else:
					s = s + 1
					p = s

			elif sum in l:
				s = s + 1
				p = s

			else:
				p = sum
				l.append(sum)
				sum = 0

		return sum


