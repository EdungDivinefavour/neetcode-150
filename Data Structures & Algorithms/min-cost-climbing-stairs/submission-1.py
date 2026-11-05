class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # So the last solution failed as predicted. Let's cut down on some of that work
        # Notice something.. that when we compute the cost of climbing from a given index, that value is never going to change
        # So there is no need to recompute it again and again and again for who knows how long
        # We can just store the result of that computation with a dictionary or array
        floors = len(cost) - 1
        memo = {}

        def getMin(i):
            # If we take some step and end up jumping too far, its not a valid step so we can't pay the cost
            if i > floors: return 0
            
            # If we've ever computed this value, no need to go deeper in DFS so just return the stored value
            if i in memo: return memo[i]

            myCost = cost[i]
            oneStep = getMin(i+1)   # If I took one step from here
            twoSteps = getMin(i+2)   # If I took two steps from here

            # Pay my cost and add it to the min between the cost of going one step and going two steps from here
            totalCostFromI = myCost + min(oneStep, twoSteps)
            
            # Store it in the dictionary
            memo[i] = totalCostFromI
            return memo[i]

        # We are allowed to start at either index 0 or 1. So return whatever is the smallest between both
        # One nice thing is that after calculating getMin(0), we basically won't be calculating anything for getMin(1) 
        # This is because all indexes that 1 could have landed on, 0 would have already calculated! So during its run, we will just be returning computed values from the map!
        res = min(getMin(0), getMin(1))
        
        return res