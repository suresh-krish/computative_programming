# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and 
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that 
# any values that would otherwise produce a consecutive run of k elements are not present. 
# For example: 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3]) 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3]) 
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on 
# that copy and return it. Instead, you must directly construct the result here.


def shortenlongruns(L, k):
	l = [L[0]]
	flag = 0
	for i in range(1,len(L)):
		if L[i]  != l[-1]:
			l.append(L[i])
		elif L[i] == l[-1]:
			sum = 1
			ind = i
			while True:
				if L[ind] == L[ind + 1]:
				    sum = sum + 1
				    ind= ind + 1
				else:
					if sum!=k:
						l.append(L[ind - 1])
						sum = 0
						i = ind - 1
						break
					else:
						i = ind - 1
						break
			# l.pop()
	return l





