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
	dic = {}
	for i in n:
		if i in dic:
			dic[i] = dic[i] + 1
		else:
			dic[i] = 1


	maxi = max(dic.values())
	l = []
	for i in dic:
		if dic[i] == maxi:
			l.append(i)

	return min(l)

		