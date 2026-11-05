class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # This solution as is, is very inefficient and need some memoization but I will submit it to show you that it fails due to its insane inefficiencies
        floors = len(cost) - 1

        def getMin(i):
            # If we take some step and end up jumping too far, its not a valid step so we can't pay the cost
            if i > floors: return 0

            myCost = cost[i]
            oneStep = getMin(i+1)   # If I took one step
            twoSteps = getMin(i+2)   # If I took two steps

            # Pay my cost and add it to the smaller between the cost of going one step and going two steps
            return myCost + min(oneStep, twoSteps)

        # We are allowed to start at either index 0 or 1. So return whatever is the smallest between both
        res = min(getMin(0), getMin(1))
        
        return res