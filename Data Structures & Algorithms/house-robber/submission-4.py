class Solution:
    def rob(self, nums: List[int]) -> int:
        # Another efficient Top Down approach(more efficient O(n) time and space) we can take to this problem is as follows:
        # Instead of looping through the remaining houses for each house, we can instead look one house at a time and decide from there
        # Remember that the question does not force us to rob all houses, it only says to return the max we can rob under those constraints
        # So we can ask at each house, "hmmm do I want to rob it or not?", if I do, what is my next step from here, and if I don't what is my next step from here?

        # So the nice thing about this approach is that we don't need to explicitly check every possible house we could rob next.
        # We simply make a decision about the house we're currently standing on, and let the recursion figure out the best result from whatever houses remain.
        # This way, we are still considering all the possibilities, but without needing that for loop from our previous solution.

        NUMS = len(nums)
        memo = {}

        def decideWhetherToRobHousesFromIndex(index):
            # If we have gone past the last house... there's nothing left to rob, so we just return 0.
            if index >= NUMS: return 0

            # Now one thing to notice is that the maximum money we can rob starting from a given index will never change.
            # It doesn't matter how we got to this house... the remaining houses and the choices we can make from here are still the same.
            # So if we've already computed the answer for this index, we can simply return it instead of calculating everything again.
            if index in memo: return memo[index]

            # If we choose to rob this house, we can take me and pass the baton to the house after the next
            robHouse = nums[index] + decideWhetherToRobHousesFromIndex(index+2)

            # If we choose to not rob the house, we can just pass the baton over to the next house
            dontRobHouse = decideWhetherToRobHousesFromIndex(index+1)

            # So we've now explored both possibilities... ie robbing this house or not robbing it.
            # Since we are trying to maximize our profit, we simply take whichever choice gave us the bigger stash.

            # Store the result of the compute in our memo
            memo[index] = max(robHouse, dontRobHouse)
            return memo[index]

        # We start from the very first house and let the recursion handle all the decisions from there.
        # And since we're memoizing each index, every house's maximum possible profit only needs to be calculated once.
        # So unlike our previous O(n^2) solution, this one takes O(n) time and O(n) space.
        return decideWhetherToRobHousesFromIndex(0)