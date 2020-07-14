"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    l = [0,1]
    for i in range(0,15,1):
        j = l[i] + l[i+1]
        l.append(j)
    return l[position]