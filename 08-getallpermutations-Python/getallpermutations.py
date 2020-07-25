# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

def permutations(x,i,l):
	if len(x) == i:
		l.append(tuple(x))

	for j in range(i,len(x)):
		x[i],x[j] = x[j],x[i]
		permutations(x,i + 1,l)
		x[i],x[j] = x[j],x[i]

	return l




def getallpermutations(x):
	i = 0
	l = []
	res = permutations(list(x),i,l)
	print(res)
	return res
