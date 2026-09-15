class Solution:
    def isPalindrome(self, s: str) -> bool:
        # A brute force way to handle this would be to remove the non-alphanumeric chars and then sort the string
        # After sorting, we would expect to see every char in pairs and then we can check based on this

        # But we can be more creative!
        # We could use two pointers. One at the start and one at the end... 
        # We expect that whatever we see on one end is what we should see at the other end
        # Ofcourse we want to skip non-alphanumeric characters while doing this

        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            # Once we find even a single l and r set that isn't the same, we can exit the entire function immediately 
            # because the string cannot be a palindrome
            if s[l].lower() != s[r].lower(): 
                return False
            
            l += 1
            r -= 1
        
        return True