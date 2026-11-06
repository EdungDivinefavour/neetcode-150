class Solution:
    # Note: This solution technically works but will fail with a Time Limit Exceeded because it is extreeeeemely inefficient.. this is because we are repeating a lot of work. 
    # I will explain more in the next solution.


    def rob(self, nums: List[int]) -> int:
        # So for this question... I like the recursive approach a lot as its just a lot easier to reason about
        # The idea is that for every single house... we want to rob that and then rob all its neighbors(and prefer the neighbor with the bigger profit)
        # But after robbing a given house, while trying to rob its neighbors, we can't rob its direct next neighbor because the alarms will go off
        # So we have to rob every house after its direct neighbor... Then we can record the biggest stash we found while robbing the neighbors.
        # So for a given house, the max total profit we can get is.. Itself, and the biggest stash from every neighbor after the very next.

        NUMS = len(nums)
        def robHousesStartingAt(index):
            money = 0 # At this point, we have no money.
            money += nums[index] # Rob this house we're standing on

            # Then proceed to rob all the houses we can rob from our allowed slots to the end
            maxFromNeighbors = 0
            for i in range(index+2, NUMS):
                res = robHousesStartingAt(i)
                maxFromNeighbors = max(maxFromNeighbors, res)
            
            return money + maxFromNeighbors

        
        maxMoney = 0
        for i in range(NUMS):
            res = robHousesStartingAt(i)
            maxMoney = max(maxMoney, res)
        
        return maxMoney
