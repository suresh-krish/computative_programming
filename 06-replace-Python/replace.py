# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	l = len(s2)
	i = s1.index(s2)
	j = i + l
	res = s1[:i] + s2 + s1[j:]
	return res


