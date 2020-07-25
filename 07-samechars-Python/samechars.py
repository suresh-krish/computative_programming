# sameChars(s1, s2) [20 pts]
# Write the function sameChars(s1, s2) that takes two strings and returns True if the two strings are composed of 
# the same characters (though perhaps in different numbers and in different orders) -- that is, if every character 
# that is in the first string, is in the second, and vice versa -- and False otherwise. This test is 
# case-sensitive, so "ABC" and "abc" do not contain the same characters. The function returns False if either 
# parameter is not a string, but returns True if both strings are empty (why?).

def samechars(s):
	s1 = s[0]
	s2 = s[1]
	if s1 == "" and s2 == "":
		return True

	elif type(s1) != str or type(s2) != str:
		return False

	elif s1 == "" or s2 == "":
		return False

	else:
		if len(s1) <= len(s2):
			for i in s1:
				if i not in s2:
					return False
			return True

		else:
			for i in s2:
				if i not in s1:
					return False
			return True

