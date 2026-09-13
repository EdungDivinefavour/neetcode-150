class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # A somewhat brute force approach would be
        # To sort both strings and then compare each ith element in s against the ith element in t
        # We would expect that if they had the same number of characters, every ith element in s should also be the ith element in t after sorting
        

        # Before wasting any compute time, if they are not of the same length, they cannot be anagrams
        if len(s) != len(t): return False

        # Now proceed to rest of checks
        s = "".join(sorted(s))
        t = "".join(sorted(t))

        for i in range(len(s)):
            el = s[i]
            if el != t[i]: return False
        
        return True