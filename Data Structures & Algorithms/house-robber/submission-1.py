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

        
        maxMoney = 0
        for i in range(NUMS):
            res = robHousesStartingAt(i)
            maxMoney = max(maxMoney, res)
        
        return maxMoney