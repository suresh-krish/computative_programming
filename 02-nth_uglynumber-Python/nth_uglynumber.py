# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.
import math


def primefac(a):
    li = []
    if a == 5:
        li.append(a)

    while a % 2 == 0:
        li.append(2)
        a = a // 2

    for i in range(3,int(math.sqrt(a) + 1),2):
        while a % i == 0:
            li.append(i)
            a =a // i

    return li



def fun_nth_uglynumber(n):
    x = 2
    p = 0
    if n == 0:
        return 1

    elif n == 1:
        return 2

    elif n == 2:
        return 3

    while p != n:
        x = x + 1
        l = primefac(x)
        if 2 in l or 3 in l or 5 in l:
            for i in l:
                if i > 5:
                    break
            else:
                p = p + 1

    return x
