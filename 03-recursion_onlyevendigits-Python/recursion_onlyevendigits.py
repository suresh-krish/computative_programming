# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.


def conversion(string,stringlen,j,lis):
	if(j >= stringlen):
		if len(lis) == 0:
			return "0"
		else :
			return lis
	if int(string[j]%2 == 0):
		lis = lis + string[j]

	return conversion(string,stringlen,j+1,lis)

def recursive (l,le,i,li):
	if(i >= le):
		return li
	li.append(int(conversion(str(l[i]),len(str(l[i])),0,"")))
	return recursive(l,le,i+1,li)


def fun_recursion_onlyevendigits(l):
	li = []

	return recursive(l,len(l),0,li)



def string_red(s,stlen,stind,news):
	if(stind>=stlen):
		if(len(news) == 0):
			return "0"
		else:
			return news
	if(int(s[stind])%2 == 0):
		news =news+s[stind]

	return string_red(s,stlen,stind+1,news)