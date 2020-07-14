# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	flag = 0
	if n < 0:
		flag = 1
	l = str(n)
	lis = list(l)
	if lis[0] == "-":
		lis.pop(0)
	if len(lis) <= int(k):
		lis.append(str(d))

	list1 = lis[::-1]
	list1[k] = str(d)
	res = list1[::-1]
	res1 = ""
	for i in res:
		res1 = res1 + i
	if flag == 1:
		res1 = "-" + res1
	return int(res1)


