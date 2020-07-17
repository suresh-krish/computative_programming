# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	l = len(s2)
	if s2 in s1:
		b = s1.count(s2)
		for i in range(0,b):
			a = s1.index(s2)
			s1 = s1[0:a] + s3 + s1[a + l:]
		return s1

