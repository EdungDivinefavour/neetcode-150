class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hopefully you are already familiar with the sliding window pattern. It is basically two pointers but we maintain some truth within those pointers.
        # So in this case, between the two pointers, we will promise that there will be no repeating characters.
        # Once we find any repeating character, we will shrink our "window" until it is repaired and we are able to maintain our truth once again.

        l, count = 0, 0
        window = set()

        # Set some pointer r to be on the right and keep moving forward
        for r in range(len(s)):

            # If our window's truth is ever broken, ie we hit a character that is already in the set, we want to keep repairing the window until our truth is fulfilled
            # We drop from the left because the repeat is somewhere behind us
            while s[r] in window:
                window.remove(s[l])
                l += 1

            # We can add our new character that we just met to the window since we are sure it will not cause a repetition at this point. As we already treated the window above
            window.add(s[r])

            # Our set will only ever hold the characters between l and r with no repitition, so its size is the same thing as the window's length
            count = max(count, len(window))

        return count