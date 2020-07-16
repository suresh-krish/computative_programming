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


def checkin(n):
	digit = sum = 0
	while(n > 0):
		digit = n % 10
		sum = sum + (digit * digit)
		n = n // 10
		return sum



def fun_nth_happy_number(n):
	if n == 0:
		return 1
	nth = 2
	p = 0
	while p!=n:
		while nth != 1 and nth !=4:
			nth = checkin(nth)
		if nth == 1:
			p = p + 1
			nth = nth + 1
		nth = nth + 1

	return nth



