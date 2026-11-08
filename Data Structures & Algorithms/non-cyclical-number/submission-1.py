class Solution:
    def isHappy(self, n: int) -> bool:
        # This is basically the same idea as the last solution, a happy number is one that eventually gets to 1, and an unhappy one will end up in a cycle
        # The only difference here is who does the checking. Last time we checked the result before recursing, now we let the next recursive call check the number it was handed
        # One important thing to note is that every call checks first, and only then does it add to seen, otherwise a number would always find itself in seen

        seen = set()
        def isCyclical(n):
            if n == 1: return False # If it stops at 1, then its not cyclical
            if n in seen: return True # If we have seen the new number it generated, then it formed a cycle and will keep cycling potentially indefinitely

            seen.add(n) # If we had never seen that newly generated number, add it to seen

            digits = [int(char) for char in str(n)] 
            res = 0

            for digit in digits: res += digit * digit
            return isCyclical(res)

        # A happy number is one that is not cyclical
        return not isCyclical(n)