class Solution:
    def rob(self, nums: List[int]) -> int:
        # So for this question... I prefer the recursive approach a lot as it's just a lot easier to reason about
        # The idea is that for every single house... we want to rob that and then rob all its neighbors (and prefer the neighbor with the bigger profit)
        # But after robbing a given house, while trying to rob its neighbors, we can't rob its direct next neighbor because the alarms will go off
        # So we have to rob every house after its direct neighbor... Then we can record the biggest stash we found while robbing the neighbors.
        # So for a given house, the max total profit we can get is.. Itself, and the biggest stash we got after robbing every neighbor after the very next.

        # One thing we can improve on from the last solution is our recomputation, eg given [2,9,8,3,6]
        # From a given house, say index 2... after computing the max profit from robbing starting from that house to the end, that value will never change regardless of how we got to index 2.
        # So when we compute that the first time, we can simply save that value and return it whenever we are asked to rob that house

        NUMS = len(nums)
        memo = {}

        # If there's only one house... there's nothing else to consider, we just rob it.
        if NUMS == 1: return nums[0]

        def robHousesStartingAt(index):
            # If we already computed the cost of robbing starting from that index, we can just return that computed value.
            if index in memo: return memo[index]

            money = 0 # At this point, we have no money.
            money += nums[index] # Rob this house we're standing on

            # Then proceed to rob all the houses we can rob from the 2nd neighbor to the right from where I stand, to the end
            maxFromNeighbors = 0
            for i in range(index+2, NUMS):
                res = robHousesStartingAt(i)
                maxFromNeighbors = max(maxFromNeighbors, res)

            memo[index] = money + maxFromNeighbors
            return memo[index]

        # Now here's something interesting... In our original solution, we were looping through EVERY single house
        # And calling robHousesStartingAt(i) on each one to find whichever starting house gave us the biggest profit.
        # But do we actually need to start from every single house?

        # Think about it... given [2,9,8,3,6], if we start by robbing 2, our recursion will already explore 8, 3 and 6.
        # And if we start by robbing 9, our recursion will explore 3 and 6.
        # So between starting at 2 and starting at 9, we've already covered all the possible houses we could start robbing from.

        # Even if the best combination starts at say 8... we could have simply robbed 2 as well,
        # Because 2 isn't adjacent to 8, and since all house values are non negative, robbing 2 can't make our profit worse.
        # So there will always be an optimal combination that includes either the first house or the second house.

        # Which means we don't actually need that outer loop anymore!
        # We can simply compare the maximum profit from robbing the first house vs robbing the second house.
        # Our recursion will handle all the other possibilities internally anyway.

        return max(robHousesStartingAt(0), robHousesStartingAt(1))