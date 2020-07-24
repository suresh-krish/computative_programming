# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.
import math


def primefac(a):
    li = []
    while a % 2 == 0:
        li.append(2)
        a = a // 2

    for i in range(3,6):
        while a % i == 0:
            li.append(i)
            a =a // i

    return li



def fun_nth_uglynumber(n):
    x = 6
    p = 5
    if n == 0 or n == 1 or n == 2 or n == 3 or n == 4 or n == 5:
        return n + 1

    while p != n:
        x = x + 1
        sum = 1
        l = primefac(x)
        if 2 in l or 3 in l or 5 in l:
            for i in l:
                if i > 5:
                    break
                else:
                    sum = sum*1

            if sum == x:
                p = p + 1

    return x
