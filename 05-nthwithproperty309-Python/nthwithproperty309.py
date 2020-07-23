# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	a = 309
	p = 0
	ch = "0123456789"
	if n == 0:
		return 309

	while p != n:
		flag = 0
		a = a + 1
		j = a
		for i in range(0,5):
			j = j * a

		j = list(str(a))
		z = set(j)
		for i in ch:
			if i not in z:
				flag = 1
				break

		if flag == 0:
			p = p + 1

	return a





	
