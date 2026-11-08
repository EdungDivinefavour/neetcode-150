class Solution:
    def isHappy(self, n: int) -> bool:
        # So a happy number is one where if we keep replacing it with the sum of the squares of its digits, we eventually end up at 1
        # The question is, what happens if we never get to 1? Well.. the numbers can't keep growing forever, so at some point they have to start repeating themselves
        # Once we see a number we have already seen, we know we are in a cycle and we will never get to 1
        # So instead of asking if a number is happy, it is easier to ask if it is cyclical, and a happy number is simply one that is not

        seen = set()
        def isCyclical(n):
            if n == 1: return False # If it stops at 1, then its not cyclical

            # Convert the digits into an array for easy iteration ie 100 becomes [1, 0, 0]
            digits = [int(char) for char in str(n)]
            res = 0

            for digit in digits:
                res += digit * digit
            
            # When we get this new result, we want to find out.. hmm have we seen this before?
            if res in seen: return True  # If we have, then we spotted a cycle

            seen.add(res) # If we haven't , add it to seen so that it can help us later with detecting cycles
            return isCyclical(res)

        # A happy number is one that is not cyclical
        return not isCyclical(n)