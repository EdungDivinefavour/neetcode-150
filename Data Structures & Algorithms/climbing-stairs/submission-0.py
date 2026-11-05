class Solution:
    def climbStairs(self, n: int) -> int:
        # There are a few ways we can solve this problem.
        # One way is to think of this from a backtracking/DFS approach shere.
        # So recall that we are only allowed to take 1 step or 2 steps... so lets say we wanted to get to step 3
        # Well from 0, we can either take one step or two steps.. This lands us in either 1 or 2..... 
        # Now from 1, we can either take one step or two steps.. Similarly from 2, we can either take one step or two steps.
        # If along the way, we land in 3 ie n, we have found one way of doing it.. So we have to add all the decisions we were able to get to.
        # So basically, it would be the sum of all the decisions we can take if we took 1 step from wherever we were + if we took 2 steps from wherever we were

        # This initial approach will likely hit a Time Limit Exceeded since it is super inefficient... But intuitively it is the easiest to reason about
        def dfs(i):
            if i == n: return 1
            if i > n: return 0

            oneStep = dfs(i+1) # If I took one step from here
            twoSteps = dfs(i+2) # If I took two steps from here

            return oneStep + twoSteps
        
        return dfs(0)
