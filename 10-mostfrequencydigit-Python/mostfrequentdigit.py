# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	d = 0
	n = str(n)
	l = list(n)
	a = l[0]
	for i in l:
		fre = l.count(i)
		if fre > d:
			d = fre
			a = i
		if fre == d:
			if i >= a:
				a = i
	return a


	