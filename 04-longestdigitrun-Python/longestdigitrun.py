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
	l = []
	for i in n:
		if i in l[-1][0]:
			l.append((i,l[-1][1] + 1))
		else:
			l.append((i,1))


	maxi = max(l[1])
	l = []
	for i in dic:
		if dic[i] == maxi:
			l.append(i)

	return int(min(l))

		