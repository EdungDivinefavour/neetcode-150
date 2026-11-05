class Solution:
    def climbStairs(self, n: int) -> int:
        # There are a few ways we can solve this problem.
        # One way is to think of this from a backtracking/DFS approach shere.
        # So recall that we are only allowed to take 1 step or 2 steps... so lets say we wanted to get to step 3
        # Well from 0, we can either take one step or two steps.. This lands us in either 1 or 2..... 
        # Now from 1, we can either take one step or two steps.. Similarly from 2, we can either take one step or two steps.
        # If along the way, we land in 3 ie n, we have found one way of doing it.. So we have to add all the decisions we were able to get to.
        # So basically, it would be the sum of all the decisions we can take if we took 1 step from wherever we were + if we took 2 steps from wherever we were

        # The reason why the previous approach is super inefficient(2^n) is because we are recomputing the same decision multiple times.
        # We can use memoization to store our computations so that we don't redo them.. this drops our T(n) to O(n)
        memo = {}
        def countWays(i):
            # If we already computed this result in the past, we can just return the result
            if i in memo: return memo[i]

            # Our base case
            if i == n: return 1 # If we hit our target, we have found a valid path
            if i > n: return 0 # If we get a bigger number, this is not a valid path

            result = (
                countWays(i+1) + # If I took one step from here
                countWays(i+2) # If I took two steps from here
            )

            # We can store the result of our computation in our dictionary
            memo[i] = result
            return memo[i]
        
        # Start ways starting from 0.. it will cap at n
        return countWays(0)
