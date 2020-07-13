# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs
import math


def fun_eggcartons(eggs):
	l = eggs/12
	l = math.ceil(l)
	return l
