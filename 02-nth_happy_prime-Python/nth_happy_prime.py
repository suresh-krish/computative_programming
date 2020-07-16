# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def checkin(n):
  digit = sum = 0
  while(n>0):
    digit = n % 10
    sum = sum + (digit * digit)
    n = n//10

  # print("sum",sum)
  return sum

def is_prime(a):
  print(a)
  flag = 0
  for i in range(2,a):
    if a % i == 0:
      flag = 1
  if flag == 0:
    print("isprime")
    return 0
  return 1
    


def fun_nth_happy_prime(n):
  if n == 0:
    return 7
  else:
    nth = 8
    res = 8
    p = 0
    while p!=n:
      print("p", p)
      # print(res)
      # printh("nth",nth)
      while nth != 1 and nth !=4:
        nth = checkin(nth)
      if nth  ==  1:
        print(res,"res")
        z = is_prime(res)
        print("z",z)
        if z !=0 :
          # p = p + 1
          res = res + 1
          nth = res
        else:
          p = p + 1
          res = res + 1
          nth = res
        
      else:
          res = res + 1
          nth = res

    return res - 1