# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22


def isprime(i):
    lis = []
    while i % 2 == 0:
        lis.append(2)
        i = i / 2




def fun_nth_smithnumber(n):
    x = 4
    if n == 0:
        return 4


    while p != n:
        x = x + 1
        p = 0
        l = isprime(x)

    return x