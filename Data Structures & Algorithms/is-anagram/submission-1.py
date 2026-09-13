class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # A better way to do this would be as follows
        # We can use extra storage to store the count of each element in one of them.. say s... so for each one we see, we can count up 1..2...3 etc for each char
        # Then we can iterate through the other(t) and check that the count of each char is the same.
        # A good way to check that the count is the same is to simply count down when we see a char ie 3...2...1 etc
        # If at the end of our count, any key in s is less than 0, then it failed the anagram check because that would mean 't' had more of that char than s had counted
        # Similarly, if at the end, any key in s is more than 0, then it also failed the check because that would mean that 't' had less of that char than s had counted

        # Before wasting any compute time, if they are not of the same length, they cannot be anagrams
        if len(s) != len(t): return False

        # Note that the below approach works because we returned early when their lengths were not the same
        A = {}
        for el in s:
            A[el] = 1 + A.get(el, 0) # If the element exists, increase its count by 1... if not, first return 0 and then increase its count by 1
            
        for el in t:
            if A.get(el) == None or A.get(el) == 0:
                return False

            A[el] -= 1

        return True