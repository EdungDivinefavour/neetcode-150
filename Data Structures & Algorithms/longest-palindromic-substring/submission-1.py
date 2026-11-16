
class Solution:
    # Same as last solution.. Just separated the 2 palindrome checks to make it easier to read
    
    def longestPalindrome(self, s: str) -> str:
        # So for this problem... we want to find the longest substring that is a palindrome.
        # Initially, I thought about starting from the first character and building the string one character at a time...
        # But the problem is that given "ababd" just because "ab" is not a palindrome doesn't mean "aba" will not be one.
        # So knowing the longest palindrome we have found so far doesn't necessarily help us determine if a bigger substring is a palindrome.

        # But think about it... a palindrome is basically a string that is the same forwards and backwards.
        # So instead of growing our substring from left to right, why not start from the MIDDLE and expand outwards?
        # Eg for "aba", we can start at "b" and check whether the characters on both sides match... and they do!
        # Then we can keep expanding until the characters no longer match or we go out of bounds.

        # Now the palindrome could be anywhere in the string... so we simply try EVERY character as a possible center.
        # Also, some palindromes have an odd length like "aba", while others have an even length like "abba".
        # So for each index, we need to try both possibilities because an even palindrome has its center BETWEEN two characters.

        # Store the start and end indices of the longest palindrome we have found.
        # We initialize them like this so that even a single character will be considered longer than our initial result.
        maxPal = (-1, -2)

        for i in range(len(s)):
            # First, let's check for odd length palindromes... ie both pointers will start on the same character.
            l, r = i, i

            # As long as our pointers are within bounds and the characters match, we have a palindrome so far.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If we find a longer palindrome, then we want to update maxPal
                if r - l > maxPal[1] - maxPal[0]:
                    maxPal = (l, r)

                # Then expand outwards one more time and see if we can make our palindrome even bigger.
                l -= 1
                r += 1

            # Now let's check for even length palindromes... ie both pointers will start on adjacent characters.
            # Eg for "abba", the middle is between the two "b"s, so we can start from those two characters and expand outwards.
            l, r = i, i+1

            # Again, as long as our pointers are within bounds and the characters match, we have a palindrome so far.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If we find a longer palindrome, then we want to update maxPal
                if r - l > maxPal[1] - maxPal[0]:
                    maxPal = (l, r)

                # Then expand outwards one more time and see if we can make our palindrome even bigger.
                l -= 1
                r += 1

        # By the time we finish checking every possible center, maxPal will contain the indices of our longest palindrome.
        # Since Python slicing excludes the ending index, we need use end+1 to include the last character.
        start, end = maxPal
        return s[start:end+1]
