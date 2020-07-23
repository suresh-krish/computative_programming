# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math

def fun_nearestkaprekarnumber(n):
    print(n)
    near = n
    start = 2
    n1 = 20
    l = [1]
    p = 0
    while p !=n1 :
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
            # print(start)
            p = p + 1
            l.append(start)

    min = 100000
    print(l)
    for i in l:
        print("i",i)
        print("n",near)
        if abs(i-near) < min:
            print(abs(i-n))
            min = i
    print("min",min)
    return min


