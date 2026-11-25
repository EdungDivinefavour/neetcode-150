
class Solution:
    # Note, this solution is not fully correct. See solution 1
    
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
        # 2. Combine me with the last char in all those valid ways, assuming the combination is valid
        #
        # But do we really need to go through all the valid ways individually?
        # If the last char + me is greater than 26, then none of those combinations can possibly be valid
        # And if the combination is valid, then we can just add the number of ways we already had again
        # Because we are assuming that every valid way can also use this new combination
        #
        # So instead of storing all the actual combinations, why don't we just store how many valid ways we have at every index?

        dp = [0] * len(s)

        for i in range(len(s)):

            # For the first char, we are assuming there is only one way to decode it
            if i == 0:
                dp[0] = 1
                continue

            # We know that atleast we will be able to use the previous element's dp since adding me separately will not change the number of ways
            # ie if we had 2 ways before, adding me separately to each of them should still give us 2 ways
            waysFromHere = dp[i-1]

            # Now lets see if we can combine me with the previous char
            # If the combination is greater than 26 or the previous char is 0, then we can't combine them
            # So we can just stick with the ways we got from adding me separately
            if int(s[i-1]+s[i]) > 26 or s[i-1] == "0":
                dp[i] = waysFromHere

            # If one way to decode by combining is correct, then all of them are correct
            # So we can just add the number of ways we previously had again
            else:
                waysFromHere += dp[i-1]
                dp[i] = waysFromHere # Sure I can clean up this repitition... will come back to it shortly

        return dp[-1]
