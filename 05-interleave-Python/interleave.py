# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	l1 = list(s1)
	l2 = list(s2)
	i = 0
	ans = ""
	while True:
		if len(l1) != 0 :
			ans = ans + l1[i]
			l1.pop(0)
		if len(l2) != 0:
			ans = ans + l2[i]
			l2.pop(0)
		if len(l1) == 0 and len(l2) == 0:
			break
		else:
			i = i + 1
	return ans


	