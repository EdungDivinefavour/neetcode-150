class Solution:
    def climbStairs(self, n: int) -> int:
        # This is a good question to introduce the idea of dynamic programming... The following is referred to as the top down approach
        # We want to know how many different ways we could have gotten to the top of n steps, taking either 1 or 2 steps at a time
        # The first thing we want to figure out is, if we were at the top, how did we even get to step n?
        # Well.. the last move we made either had to be either a 1 step or a 2 step. There is no other way
        
        # If it was a 1 step, then we were standing on n-1 before it. If it was a 2 step, then we were standing on n-2 before it
        # So every way of reaching n-1 gives us a way to reach n, and every way of reaching n-2 also gives us a way to reach n
        # Which means ways(n) = ways(n-1) + ways(n-2)
        
        # So the first thought might be to just recurse on this... It technically works, but there is a catch
        # To compute ways(5) we need ways(4) and ways(3). But ways(4) also needs ways(3).. so ways(3) ends up being computed twice
        # And that keeps compounding the deeper we go, so we end up redoing the same steps over and over and over
        # That is what makes n=45 so slow, we are doing exponential work for something that only has 45 unique answers
        # So instead of recomputing, we can store the answer for every step the first time we figure it out in a hashmap

        memo = {}

        def ways(n):
            # If we have already stored the result of this computation in the past, we can just hand it back
            if n in memo: return memo[n]

            # Base cases, there is 1 way to reach step 1 and 2 ways to reach step 2 (1+1 or 2)
            if n <= 2: return n

            # Otherwise, the ways to reach n is basically the ways to reach n-1 plus the ways to reach n-2
            # Note that we call ways and not climbStairs here, because climbStairs would create a brand new memo every call and we would lose everything we stored
            memo[n] = ways(n-1) + ways(n-2)
            return memo[n]
        
        return ways(n)