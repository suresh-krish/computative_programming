# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.



def fixmostlymagicsquare(L):
	for  i in range(len(L)):
		for j in range(len(L)):
			sum = 0
			ch = 0
			for k in range(len(L)):
				sum = sum + L[i][k]
				print(L[i][k])
				print(L[k][j])
				# print(sum,ch)
				ch = ch + L[k][j]
				print(sum,ch)

			if sum != ch:
				z  = ch - sum
				z = abs(z)
				L[i][k] = L[i][k] - z
	
	
	
	return L