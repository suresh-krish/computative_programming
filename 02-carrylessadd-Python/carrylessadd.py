# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	x = str(x)
	x = x[::-1]
	y = str(y)
	y = y[::-1]
	i = 0
	res = ""

	while True:
		sum = 0
		if len(x) -1 < i and len(y) - 1 < i:
			return int(res)
		if len(x) - 1 >= i:
			sum = sum + int(x[i])

		if len(y) - 1 >= i:
			sum = sum + int(y[i])

		r = sum%10
		res = str(r) + res
		i = i + 1



