class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Unlike the last approach which starts from the big question ie we have these giant stairs to climb, how do we get to the top?
        # Which is referred to as Top down(I know the name is confusing seeing as we were looking from bottom of the stairs and trying to climb up)..
        # Its not really about stairs or no stairs, top down basically refers to the approach where you start from a big problem and ask, how do I start from this big problem to the small one.

        # Anyway... In this solution, we are instead using the Bottom Up approach here, which basically asks... If we started from the very smallest problem, how does it lead us to solving the big problem?

        # In our case, we can simply start at the top of the stairs and ask.. "What is the minimum cost to rob from here"?
        # Then go down one stair and ask, "okay starting from here now, what is the minimum cost to rob from here?" and so forth

        minCost = 0
        dp = [0] * len(cost) # We can use a table to store the computation we have gotten so far

        # So dp[i] basically represents the minimum cost of reaching the top if we started from stair i.
        # And since we're starting from the end, by the time we get to any given stair, we would have already computed the minimum cost from the stairs after it.

        # Since we want to start from the end of the stairs, we have to loop backwards
        for i in range(len(cost) -1, -1, -1):
            if i == len(cost) - 1:
                # If we are at the very last stair... we will just pay for this stair and we're done.
                # There is nothing else to calculate because the next step takes us to the top.
                dp[i] = cost[i]
                continue

            if i == len(cost) - 2:
                # If we are at the second last stair, we can either step directly to the top
                # Or step on the last stair first... so we just want to take whichever is cheaper.
                dp[i] = min(cost[i], cost[i] + cost[i+1])
                continue

            # Now for every other stair... we know that after paying for this stair, we have two choices ie We can move one stair or two stairs forward.
            # But the nice thing is that we already calculated the minimum cost from both of those stairs.
            # So we don't need to explore all the possibilities again... we just need to take the cheaper of the two.
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        # And since the problem allows us to start from either stair 0 or stair 1...
        # We simply return whichever one has the smaller total cost of reaching the top.
        return min(dp[0], dp[1])