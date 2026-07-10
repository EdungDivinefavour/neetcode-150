class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        A = {}
        for val in s:
            A[val] = A.get(val, 0) + 1
        
        for val in t:
            if A.get(val) == None or A.get(val) <= 0:
                return False
            A[val] -= 1
        
        return True
