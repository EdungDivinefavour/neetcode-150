
class Solution:
    def rob(self, nums: List[int]) -> int:
        # So for this question... just like in House Robber 1, at each house we are still asking ourselves the same question...
        # Do we want to rob this house or not? If we rob it, what happens next? And if we don't, what happens next?
        # But there is one important difference this time... the houses are arranged in a CIRCLE!
        # Which means that the first house and the last house are now adjacent to each other.
        # So if we rob the first house, we can't rob the last one, and vice versa.

        # Recall that in our previous solution, we solved this problem twice...
        # So in one scenario, we simply pretended the last house didn't exist. And in the other scenario, we pretended the first house didn't exist : )
        # Then we compared the maximum profit from both scenarios.

        # Now here is another way to implement that same idea...
        # Instead of using a separate function to define the range of houses we are allowed to rob, we can use a flag!
        # This flag basically tells us whether the LAST house is forbidden in our current scenario.
        # If the flag is True, we are not allowed to rob the last house. Otherwise, we can consider it normally.

        if len(nums) == 1: return nums[0]

        # Now one interesting thing about memoization here is that index alone is not enough to identify our subproblem.
        # Because the maximum profit from a given index could be different depending on whether the last house is forbidden or not.
        # So instead of using a dictionary with just index as our key, we can use a 2D array to store both possibilities.
        # memo[i][0] represents the maximum profit from index i when the last house is allowed.
        # memo[i][1] represents the maximum profit from index i when the last house is forbidden.
        # We initialize everything to -1 because that tells us we have not computed the result for that state yet.

        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            # If we have gone past the last house, there is nothing left to rob, so we just return 0.
            # Also, if we are standing at the last house and our flag is True, we are not allowed to rob it.
            # So we return 0 in that case as well.
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0

            # If we have already calculated the maximum profit for this index and flag combination, we can simply return it.
            if memo[i][flag] != -1:
                return memo[i][flag]

            # Now just like House Robber 1, we have two choices... either rob this house or skip it.
            # If we skip it, we collect nothing and simply pass the baton to the next house, keeping our current flag.
            # If we rob it, we collect its money and pass the baton two houses forward because we can't rob the next house.
            # We also pass along whether the last house is forbidden... and if we are robbing the first house, that flag must be True.
            # So flag or (i == 0) makes sure that once the first house is robbed, the last house will remain forbidden.
            # We then take whichever choice gives us the bigger stash.
            res = max(
                dfs(i + 1, flag),
                nums[i] + dfs(
                    i + 2, flag or (i == 0)
                )
            )

            # Since we have now computed the maximum profit for this exact state, we can store it in our memo.
            # That way, if we ever reach the same index with the same flag again, we don't have to recompute everything.
            memo[i][flag] = res

            return memo[i][flag]

        # Now we solve our two scenarios...
        # Scenario 1: Start from the first house with flag=True, meaning we are excluding the last house entirely.
        # Scenario 2: Start from the second house with flag=False, meaning we are excluding the first house and allowing the last house.
        # Notice that in the first scenario, we can still choose to skip the first house... we are simply forbidding the last house.
        # And since every valid combination must exclude either the first house or the last house (or both), these two scenarios cover everything.
        # So we can simply return whichever one gives us the bigger stash.

        # And since each index has at most two possible states, we only have O(n) subproblems.
        # So our time complexity is O(n), and our space complexity is also O(n) for the memo and recursion stack.
        return max(dfs(0, True), dfs(1, False))
