# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	shift1 = "abcdefghijklmnopqrstuvwxyz"
	shift2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	s1 = list(shift1)
	sl1 = len(s1) - 1
	s2 = list(shift2)
	sl2 = len(s2) - 1
	ans = ""
	for i in msg:
		if i in s1:
			a = s1.index(i)
			j = a + shift
			if j > sl1:
				j = j - sl1 - 1
			ans = ans + s1[j]
		elif i in s2:
			a = s2.index(i)
			j = a + shift
			if j > sl2:
				j = j - sl1 - 1
			ans = ans + s2[j]
		else:
			ans = ans + i
	return ans





