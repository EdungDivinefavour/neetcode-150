
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # I knew it couldn't have been so easy :/ Now I see the problem with the last approach.
        # We were committing to the first slice that produces a word... and never looking back after that.

        # This is a problem because imagine s = "abcd" and wordDict = ["a", "abc", "d"]
        # Our previous solution will first cut out 'a', then be left with 'bcd' but because it cannot cut 'bcd' any further it will return false.... meanwhile we could have cut it as 'abc' and 'd'

        # So instead of committing to the first slice we see during our traversal... We can/should try out all the slices we can form from any given position
        # That means we first try 'a'.. then 'ab' then 'abc' then 'abcd'... And for every valid slice we find, we also want to try every possible slice from where it ends

        # At every slice, we want to return True if that slice is in our dictionary AND we can successfully break everything that comes after it
        # We don't need every child to be valid though... we just need to find ONE path that works

        words = set(wordDict) # I think we still need our set for quick lookup
        LEN = len(s)
        memo = {}

        def sliceStringFrom(start):
            # If we have already figured out whether the string can be broken from this position, no need to do all that work again
            if start in memo: return memo[start]

            # If we have reached the end of the string, that means we have successfully broken everything before here into valid words
            # So there is nothing left to figure out... we can just return True
            if start == LEN: return True

            # Recursively try using one char from here, then two from here etc etc till the end by moving our right pointer one forward
            # The idea is to see if any of the slices we get from here will lead us to a valid solution
            r = start + 1

            while r <= LEN:
                # First lets check if everything from start till here is valid... If it is not, we can skip it and try its siblings... no need to pass the baton unto its children
                isValid = s[start:r] in words
                if not isValid:
                    r += 1
                    continue

                # But if it is valid, we are interested in it.. so lets check whether every child decision after this slice can also be broken into valid words
                # Notice that we start from r because that is exactly where our current slice ends
                isChildValid = sliceStringFrom(r)

                # If we also find a valid child path, that means both our current slice and everything after it are valid
                # So we have found a successful way to break the string from this position... no need to keep checking the other siblings since the question says to return True when we find it
                if isChildValid:
                    memo[start] = True
                    return memo[start]

                r += 1

            # If we get here, that means we have tried every possible slice from this position and none of them led to a valid solution
            # We also want to remember this failed result so that we don't waste time exploring the same dead end again
            memo[start] = False
            return memo[start]
            
        return sliceStringFrom(0)
