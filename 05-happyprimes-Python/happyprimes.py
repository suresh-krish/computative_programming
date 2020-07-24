# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def isprime(a):
    for i in range(2,a//2 + 1):
        if a % i == 0:
            return False
    return True


def squares(a):
    sum = 0
    while a != 0:
        b = a % 10
        sum = sum + b * b
        a = a // 10

    return sum



def ishappyprimenumber(n):
    p = n
    z = isprime(n)
    while p != 1 and p != 4:
        p = squares(p)


    if p == 1:
        return True
    return False