# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math

def fun_nth_lefttruncatableprime(n):
    if n == 0:
        return 2
    prime = []
    for i in range(3,500,2):
        flag = 0
        for j in range(2,int(math.sqrt(i) + 1)):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            prime.append(str(i))

    p = 0
    print(prime)
    for i in prime:
        if "0" not in i:
            if len(i) == 1:
                p = p + 1
            else:
                res = i[1:]
                if len(res) > 2:
                    if res[1:] in prime and res in prime:
                        p = p + 1
                else:
                    if res in prime:
                        p = p + 1

        if p == n:
            return int(i)
    
