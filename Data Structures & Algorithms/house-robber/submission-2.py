class Solution:
    def rob(self, nums: List[int]) -> int:
        # Solution 1 was a rather brute force solution even after memoization. Because for each house we were still doing all the combinations we could form
        # We can instead think of this problem from a proper DP approach (Top Down)
        # Which basically means that we start with our big problem and then start breaking it into smaller and smaller problems till we hit our base case
        # So given say [2,9,8,3,6], the question now is.. How do we break down the problem into smaller ones?

        # Well starting from the first house, we want to get the max from either robbing it or not robbing it.
        # When at a house, if we are robbing it, we want to pass the smaller subproblem over to the next house we can rob
        # If we are not robbing it, we can just pass the baton over to the next index and ask the same question when we get there

        # Now on its own this will still be slow, because the same house can be reached in multiple ways eg given [2,9,8,3,6]
        # Index 3 can be reached from index 1 (we robbed it and jumped 2) and also from index 2 (we skipped it).. so we end up solving index 3 over and over
        # But from a given house, the max we can get from there to the end would never change regardless of how we got there
        # So once we compute it, we can save it in memo and just return that computed value the next time we are asked

        NUMS = len(nums)
        memo = {}

        def robHousesStartingAt(index):
            # If we already computed the max loot starting from this index, we can just return it
            if index in memo: return memo[index]

            # If we have gone past the last house, there is nothing left to rob
            if index > NUMS-1: return 0

            # If we are standing on the last house, there is nothing else to choose from so we just rob it
            if index == NUMS-1: return nums[NUMS-1]

            # Either we rob this house and hop over to the one after the next, or we skip this house and ask the same question from the next one
            maxLoot = max(
                nums[index] + robHousesStartingAt(index + 2),
                robHousesStartingAt(index+1)
            )

            memo[index] = maxLoot
            return memo[index]

        # We are starting from the first house, which is our big problem
        return robHousesStartingAt(0)