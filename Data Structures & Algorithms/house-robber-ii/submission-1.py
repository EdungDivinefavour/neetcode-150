
class Solution:
    def rob(self, nums: List[int]) -> int:
        # So for this question... just like in House Robber 1, at each house we are still asking ourselves the same question...
        # Do we want to rob this house or not? If we rob it, what happens next? And if we don't, what happens next?
        # But there is one important difference this time... the houses are arranged in a CIRCLE!
        # Which means that the first house and the last house are now adjacent to each other.
        # So if we rob the first house, we can't rob the last one, and vice versa.

        # Initially, we tried solving this by keeping track of all the houses we had robbed using a set.
        # But you see, we don't actually need to remember every house we had robbed... Because our index+2 jump already takes care of preventing us from robbing adjacent houses.
        # The only additional thing we needed to remember was whether we had robbed the FIRST house.
        # Because that is the only earlier decision that could affect whether we are allowed to rob the LAST house.

        # But here is an even simpler way to think about this...
        # Since we know that we can NEVER rob both the first and last house, why not just solve the problem twice?
        # In one scenario, we simply pretend the last house doesn't exist.... And in the other scenario, we pretend the first house doesn't exist : )
        # Then we can just take whichever scenario gives us the bigger stash!

        # And think about it... we are not missing any valid combinations by doing this.
        # Because every valid combination must either exclude the first house or exclude the last house (or both).
        # So between those two scenarios, we are guaranteed to have considered every possible valid combination.

        NUMS = len(nums)

        # If there is only one house... there is no real circular constraint to worry about. We can simply rob that house and return its money.
        if NUMS == 1: return nums[0]

        def robHouses(start, end):
            # So this function basically solves our original House Robber 1 problem... except instead of considering the entire array, we are only considering houses from start to end.
            # This way, we can reuse the exact same Top Down approach we already figured out.

            # We give each scenario its own memo because the maximum money we can rob from a given index could be different depending on where our allowed range ends.
            # So by keeping separate memos, we can safely use just index as our memoization key.
            memo = {}

            def dfs(index):
                # If we have gone past the last house we are allowed to consider... there is nothing left to rob, so we just return 0.
                if index > end: return 0

                # Recall that the maximum profit from a given index will always be the same as long as we are solving within the same allowed range.
                # So if we have already computed the answer for this index, we can simply return it.
                if index in memo: return memo[index]

                # If we choose to rob this house, we can collect its money and pass the baton two houses forward because obviously we can't rob the house immediately after it.
                robMe = nums[index] + dfs(index+2)

                # If we choose NOT to rob this house, we can collect nothing from it... and we can simply pass the baton to the very next house.
                dontRobMe = dfs(index+1)

                # So now we have explored both possibilities... robbing this house or skipping it.
                # We just take whichever gives us the bigger stash and save that result in our memo so we don't have to recompute everything if we reach this index again.
                memo[index] = max(robMe, dontRobMe)
                return memo[index]

            # Start from the first house in our allowed range and let recursion handle the rest.
            return dfs(start)

        # Now we can solve our two scenarios...
        # Scenario 1: Consider every house EXCEPT the last one, ie indices 0 to NUMS-2.
        # Scenario 2: Consider every house EXCEPT the first one, ie indices 1 to NUMS-1.
        # And since every valid combination belongs to at least one of these scenarios, we can simply return whichever one gives us the maximum profit.

        # And the nice thing is that each scenario is just our O(n) Top Down House Robber 1 solution.
        # So even though we are solving it twice, O(n) + O(n) is still O(n) time.
        # And because we are only storing O(n) memoized results and using an O(n) recursion stack, our space complexity is also O(n).

        return max(
            robHouses(0, NUMS-2),
            robHouses(1, NUMS-1)
        )
