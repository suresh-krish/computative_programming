# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    l = 0
    res = ""
    if s1 == "" or s2 == "":
        return ""

    else:
        for i in range(len(s2)):
            for j in range(i + 1, len(s2)):
                c = s2[i:j]
                if c in s1:
                    if len(c) > l:
                        l = len(c)
                        res = c

        return res

