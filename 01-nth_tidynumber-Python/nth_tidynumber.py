# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def fun_nth_tidynumber(n):
    p = 0
    x = 0
    while p != n:
        x = x + 1
        if x >0 and x < 10:
            p = p + 1

        else:
            s = str(x)
            for i in range(len(s)-1,0,-1):
                if int(s[i]) < int(s[i + 1]):
                    break

            else:
                p = p + 1


    return x + 1

