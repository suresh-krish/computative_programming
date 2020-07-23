# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22


def isprime(n):
    i = 2
    lis = []
    while i*i <= n:
        if n % i:
            i += 1
        else :
            n //= i
            lis.append(i)
    if n > 1:
        lis.append(n)

    return lis





def fun_nth_smithnumber(n):
    x = 4
    p = 0
    if n == 0:
        return 4


    while p != n:
        x = x + 1
        l = isprime(x)

        sum = 0
        for i in l:
            while i != 0:
                p = i % 10
                sum = sum + p
                i = i // 10

        res = 0
        ch = x
        while x != 0:
            p = x % 10
            res = res + p
            ch = ch // 10

        if res == sum:
            p =p + 1


    return x