class Solution:
    # There is an even more optimal way to solve this problem compared to the previous one.
    # Instead of using a whole table to store our computations, we can simply just store the two most recent computations because that all we care about for calculating the next.

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Recall that in this solution, we are using the Bottom Up approach, which basically asks... If we started from the very smallest problem, how does it lead us to solving the big problem?
        # In our case, we can simply start at the top of the stairs and ask.. "What is the minimum cost to rob from here"?
        # Then go down one stair and ask, "okay starting from here now, what is the minimum cost to rob from here?" and so forth

        # So since we know the result of the last 2 computations, we can just hardcode them
        oneStep, twoSteps = cost[-2], cost[-1]
        

        # So oneStep basically represents the minimum cost of reaching the top if we started from oneStep from where we are currently.. and twoStep represents the same but for if we took twoSteps.
        # And since we're starting from the end, by the time we get to any given stair, we would have already computed the minimum cost from the stairs after it.

        # Since we want to start from the end of the stairs, we have to loop backwards... We already stored values for the last 2 steps above, so we want to start from the the 3rd from the end
        for i in range(len(cost) -3, -1, -1):
            # For every other stair... we know that after paying for this stair, we have two choices ie We can move one stair or two stairs forward.
            # But the nice thing is that we already calculated the minimum cost from both of those stairs.
            # So we don't need to explore all the possibilities again... we just need to take the cheaper of the two.
            
            # Temporarily store the cost of climbing from stair i
            temp = cost[i] + min(oneStep, twoSteps)

            twoSteps = oneStep # Then set twoSteps to be where oneStep was before
            oneStep = temp # Then set oneStep to be what we just calculated

            # This way when the next i wants to be calculated, oneStep and twoSteps will be in their newly updated position

        # And since the problem allows us to start from either stair 0 or stair 1...
        # We simply return whichever one has the smaller total cost of reaching the top.
        return min(oneStep, twoSteps)