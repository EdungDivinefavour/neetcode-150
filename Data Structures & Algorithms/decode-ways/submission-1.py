
class Solution:
    def numDecodings(self, s: str) -> int:
        # So my first thought is to approach this problem by going from the smallest problem to the biggest
        # ie if we already know all the ways to decode a particular string, can we somehow use that to figure out the ways to decode it after adding one more char?

        # Let's take 1426 for example
        # For 1, we have 1 way ie 1
        # For 14, we have 2 ways ie 1 4 and 14
        # For 142, we have 2 valid ways ie 1 4 2 and 14 2
        #
        # Now when we meet 6, what can we do?
        # Well, we can either add 6 separately to all the valid ways we already had
        # ie 1 4 2 6 and 14 2 6
        #
        # OR we can try combining 6 with the last char in each of those ways
        # ie 1 4 26 and 14 26
        #
        # So basically for every new char, we want to try two things
        # 1. Add me separately to all the valid ways we already had
        # 2. Combine me with the previous char, assuming the combination is valid
        #
        # But do we really need to go through all the valid ways individually?
        # If we already know how many valid ways we had before, then adding me separately should give us that same number of ways
        # And if combining me with the previous char is valid, then maybe we can just add that same number again?
        #
        # Well... that was the assumption in our first solution but it doesn't always work
        #
        # Let's say we have 226
        # When we get to 22, we have 2 valid ways
        # 2 2
        # 22
        #
        # Now when we meet 6, adding it separately works for both
        # 2 2 6
        # 22 6
        #
        # But what if we tried combining 6 with the last char in both?
        # 2 26 is valid
        # 226 is not valid
        #
        # So we can't just assume that because 26 is valid, every single arrangement we had before can also combine with 6
        # Because some of those arrangements might have already combined the previous char with another char
        #
        # So how do we fix that?
        # If we want to combine 2 and 6 into 26, why don't we just look at the ways we had before that 2?
        # ie instead of looking at all the ways of decoding 22, we look at all the ways of decoding just the first 2
        # Then we can simply add 26 to every single one of those ways
        #
        # This makes sense because we are no longer trying to combine 6 with whatever the last group happened to be
        # We are specifically combining the previous char and me into one group
        # So we shouldn't include the previous char in the ways we are extending.. since it is already part of our new group
        #
        # And that's why we use dp[i-2] when combining instead of dp[i-1]
        # But when adding me separately, dp[i-1] is still fine because we aren't changing any of the previous groups
        #
        # One other thing we have to consider is 0
        # We can't just add 0 separately because it doesn't represent any letter
        # But we can still combine it with the previous char if that gives us something between 10 and 26

        dp = [0] * len(s)

        for i in range(len(s)):

            # For the first char, we are assuming there is only one way to decode it.. unless it is 0
            if i == 0:
                dp[0] = 1 if s[0] != "0" else 0
                continue

            # We know that we can use the previous element's dp since adding me separately will not change the number of ways
            # But this only works if I am not 0.. because 0 cannot stand on its own
            if s[i] != "0":
                dp[i] += dp[i-1]

            # Now lets see if we can combine me with the previous char
            # If combining both of us gives a number between 10 and 26, then we know that combination is valid
            if 10 <= int(s[i-1:i+1]) <= 26:

                # Since we are combining two chars, we want to add that combination to all the valid ways we had BEFORE those two chars
                # ie for 226, when we get to 6, we want to combine 26 and then add it to the ways we had for the first 2
                # So we use dp[i-2] instead of dp[i-1]
                #
                # But what if we are at index 1?
                # Then there is nothing before the two chars we are combining
                # So if the combination is valid, we have exactly one way to use it by itself
                dp[i] += dp[i-2] if i >= 2 else 1

        return dp[-1]