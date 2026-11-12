class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # So for this question, we want to cut the string up into pieces such that every single piece is a palindrome
        # The first thing we want to figure out is.... how do we decide where to cut?
        # Well.. if we are standing at some index, the first piece can end at any index from there to the end of the string
        # So we can try every single one of them, and the first piece is only worth keeping if it is a palindrome
        # If it is, we take it and then do the exact same thing for whatever is left of the string
        # If we get to the end of the string, it means every piece we picked along the way was a palindrome, so we have found a valid partition

        LENGTH = len(s)
        memo = {}
       
        # Quick helper function to check if a string is a palindrome.. added some memoization too to speed things up
        # The same substring can be checked many times by different paths, eg "aa" can come up from a lot of different starting points
        # So once we know the answer for a substring, we can store it and return it the next time
        def isPalindrome(s):
            if s in memo: return memo[s]

            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]: 
                    memo[s] = False
                    return memo[s]
                else:
                    l, r = l + 1, r - 1
            memo[s] = True
            return memo[s]

        
        out = []
        def backtrack(start, path):
            # If start has gone past the last character, there is nothing left to cut, so path is holding a full partition
            if start == LENGTH:
                out.append(path[:])
                return

            # Try every possible end for the piece that starts at start
            # We are going up to LENGTH + 1 because the slice excludes the end index, and we want the last character to be included too
            for end in range(start + 1, LENGTH + 1):
                substring = s[start:end]

                # If this piece is not a palindrome, then there is no point cutting it here, so we can move on to the next end
                if isPalindrome(substring):
                    # Take this piece, then repeat the same process for whatever is left, which starts at end
                    path.append(substring)
                    backtrack(end, path)

                    # When we are done exploring that, we should remove the piece so that the next end can have its own try
                    path.pop()
                    
        backtrack(0, [])
        return out