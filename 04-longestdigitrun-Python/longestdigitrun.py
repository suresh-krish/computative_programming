# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	if n < 0:
		n = abs(n)

	n = str(n)
	for i in range(0,len(n)-1):
		b  = 0
		for j in range(i+1,len(n)-1):
			if n[i] != n[j]:
				break
			else:
				a = n[j]
				b = b + 1


		