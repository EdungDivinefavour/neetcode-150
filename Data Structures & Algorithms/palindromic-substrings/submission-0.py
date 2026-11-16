class Solution:
    def countSubstrings(self, s: str) -> int:
        # So for this problem... we want to count how many substrings in our string are palindromes.
        # This is basically the same problem as Longest Palindromic Substring see: https://github.com/EdungDivinefavour/neetcode-150/blob/master/Data%20Structures%20%26%20Algorithms/longest-palindromic-substring/submission-1.py
        # except instead of finding the longest one, we want to count ALL of them.
        # And since we already figured out how to expand around the center in the last problem, we can use that same approach here.

        # Recall that a palindrome is basically a string that is the same forwards and backwards.
        # So instead of growing our substring from left to right, we can start from the MIDDLE and expand outwards.
        # Eg for "aba", we can start at "b" and check whether the characters on both sides match... and they do!
        # Then we can keep expanding until the characters no longer match or we go out of bounds.

        # Now the palindrome could be anywhere in the string... so we simply try EVERY character as a possible center.
        # Also, some palindromes have an odd length like "aba", while others have an even length like "abba".
        # So for each index, we need to try both possibilities because an even palindrome has its center BETWEEN two characters.

        # One thing to notice is that every single character is already a palindrome by itself.
        # So for a string of length n, we are guaranteed to have at least n palindromic substrings.
        # And every time we successfully expand outwards, we have discovered another palindrome, so we can simply increase our count.

        count = 0

        for i in range(len(s)):
            # First, let's check for odd length palindromes... ie both pointers will start on the same character.
            l, r = i, i

            # As long as our pointers are within bounds and the characters match, we have a palindrome so far.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Since we have found a valid palindrome, we can increase our count.
                count += 1

                # Then expand outwards one more time and see if we can find another palindrome.
                l -= 1
                r += 1

            # Now let's check for even length palindromes... ie both pointers will start on adjacent characters.
            # Eg for "abba", the middle is between the two "b"s, so we start from those two characters and expand outwards.
            l, r = i, i+1

            # Now you might wonder... since we have two while loops, won't we accidentally count the same palindrome twice?
            # Well no... because our first loop starts with one character and only finds odd length palindromes ie lengths 1, 3, 5, etc.
            # But this second loop starts with two adjacent characters and only finds even length palindromes ie lengths 2, 4, 6, etc.
            # So a single character can NEVER be counted by this second loop, and neither loop can count a palindrome found by the other : )

            # Again, as long as our pointers are within bounds and the characters match, we have found another palindrome.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # So we increase our count for every successful expansion.
                count += 1

                # Then expand outwards again and see if we can find an even bigger palindrome.
                l -= 1
                r += 1

        # By the time we finish checking every possible center, we would have counted every palindromic substring.
        # And since we are counting occurrences, even identical substrings at different positions will be counted separately.
        return count
