class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # If the value at the left pointer is not alphanumeric, skip and try again
            if not s[l].isalnum():
                l += 1
                continue

            # # If the value at the right pointer is not alphanumeric, skip and try again
            if not s[r].isalnum():
                r -= 1
                continue
            
            # If they are both alphanumeric but aren't equal, then the string is not a palindrome
            if s[l].lower() != s[r].lower(): return False

            # But if they match, then we can advance both pointers and keep checking
            l += 1
            r -= 1

        return True