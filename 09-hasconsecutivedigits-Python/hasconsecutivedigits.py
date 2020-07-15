# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	n = str(n)
	if len(n) == 1:
		return False
	else:
		i = 0
		res = False
		while True:
			if n[i] == n[i+1]:
				res = True
				break
		return res