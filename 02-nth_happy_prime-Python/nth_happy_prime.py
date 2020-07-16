# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def checkin(n):
  digit = sum = 0
  while(n>0):
    digit = n % 10
    sum = sum + (digit * digit)
    n = n//10

  # print("sum",sum)
  return sum


def fun_nth_happy_prime(n):
	if n == 0:
		return 1
	nth = 2
	res = 2
	p = 0
	while p!=n:
    # print("p", p)
    # printh("nth",nth)
		while nth != 1 and nth !=4:
			nth = checkin(nth)
		if nth % 2 ==  0:
			p = p + 1
			res = res + 1
			nth = res
		else:
		    res = res + 1
		    nth = res

	return nth - 1

	return 0