# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def palindrom(i):
	if i == rotate(i):
		return True

	return False

def rotate(a):
	sum = 0
	while a!=0:
		k = a % 10
		sum = (sum * 10) + k
		a = a // 10

	return sum


def nthlychrelnumbers(n):
	maxi = 25
	x = 195
	p = 0

	while p != n:
		x = x + 1
		num = x
		flag = 0
		for i in range(maxi):
			num  = num + rotate(num)
			if palindrom(num):
				flag = 1
				break

		if flag == 0:
			p = p + 1

	return x