class Solution:
    # I will do you one better : ) As crazy as it sounds, there is an even shorter way!! (Although this modifies the input array)
    # So, let's give this some thought.... Do we even really need the two variables? 
    # What if we use our costs array as a DP array! So when we compute the cost for an index, we can just store it in our cost array!

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Recall that in this solution, we are using the Bottom Up approach, which basically asks... If we started from the very smallest problem, how does it lead us to solving the big problem?
        # In our case, we can simply start at the top of the stairs and ask.. "What is the minimum cost to climb from here"?
        # Then go down one stair and ask, "okay starting from here now, what is the minimum cost to climb from here?" and so forth

        # Since we want to start from the end of the stairs, we have to loop backwards... We already stored values for the last 2 steps above, so we want to start from the the 3rd from the end
        for i in range(len(cost) -3, -1, -1):
            # For every other stair... we know that after paying for this stair, we have two choices ie We can move one stair or two stairs forward.
            # But the nice thing is that we already calculated the minimum cost from both of those stairs.
            # So we don't need to explore all the possibilities again... we just need to take the cheaper of the two.
            cost[i] += min(cost[i+1], cost[i+2])
            
        # And since the problem allows us to start from either stair 0 or stair 1... and we have now replaced each element in costs with its min cost from that index,
        # We simply return whichever one has the smaller total cost of reaching the top.
        return min(cost[0], cost[1])