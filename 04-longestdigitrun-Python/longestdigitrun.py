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
	l = [(0,0),]
	for i in n:
		if int(i) == l[-1][0]:
			l.append((i,l[-1][1] + 1))
		else:
			l.append((i,1))


	maxi = max(i[1] for i in l)
	li = []
	for i in l:
		if i[1] == maxi:
			li.append(i[0])

	return int(min(li))

		