# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def fun_nth_kaprekarnumber(n):
    start = 2
    p = 0
    if n == 0:
        return 1

    while p !=n :
        start = start + 1
        a = start * start
        st = str(a)
        b = len(st)
        nth = b // 2
        res = 0
        res1 = 0
        res2 = 0
        ress = 0
        if st[:nth] != "":    
            res = res + int(st[:nth])
            if len(st[:nth - 1]) > 2:
                res1 = int(st[:nth-1])
                res2 = int(st[:nth-2])
        else:
            res = res + 0

        if st[nth:] != "":
            res = res + int(st[nth:])
            if res2 > 1:
                ress = ress + int(st[nth:])
        else:
            res = res + 0

        if int(res) == start or res1 + ress == start or res2 + ress == start:
            print(start)
            p = p + 1

    return start


    