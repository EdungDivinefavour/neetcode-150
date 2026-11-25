class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # So for this problem... we want to find the minimum number of coins we need to make up our target amount.
        # And since we can reuse each coin as many times as we want, we have two choices at every coin...
        # Either use that coin again, or skip it and move on to the next coin.

        # We can solve this recursively using backtracking, but the problem is that we might end up calculating the same subproblems over and over again.
        # So we can use memoization to remember the results we've already computed.

        LEN = len(coins)
        memo = {}

        def minCoinsFromIndex(index, total, coinCount):
            # Now one important thing here is figuring out what makes a subproblem unique.
            # Initially I thought we could simply use index as our key... but that is not enough.
            # Because we could be standing on the same coin, but have completely different totals and coin counts.
            # And since our function returns the total number of coins we have used so far, coinCount also affects the result.
            # So for this particular implementation, we need to use all three values to identify the exact same subproblem.
            key = (index, total, coinCount)

            # If we've already calculated the minimum number of coins for this exact situation...
            # We can simply return that result instead of exploring all the possibilities again!.
            if memo.get(key, None): return memo[key]

            # If we managed to reach the target amount, then this is a valid combination.
            # So we return however many coins we used to get here.
            if total == amount: return coinCount

            # But if we have gone past the last coin, or exceeded our target amount...
            # Then this path is invalid, so we can return infinity because we don't want to choose this path when calculating the minimum.
            if index >= LEN or total > amount: return float('inf')

            # From here, we can do one of two things....

            # Use me one more time(ie add me to total and pass the baton to me again)
            total += coins[index]
            useMeAgain = minCoinsFromIndex(index, total, coinCount+1)
            total -= coins[index] # Backtrack

            # Or don't use me this time(ie just pass the baton to the next guy)
            dontUseMe = minCoinsFromIndex(index+1, total, coinCount)
            # Notice above that we only want to increase count if we actually used me because we only want to count the paths that we used


            # So now that we have explored both choices... we can just take whichever one gave us the smaller coin count.
            # And since this result will always be the same whenever we encounter this exact state again,
            # We can store it in our memo instead of having to recompute everything.
            memo[key] = min(useMeAgain, dontUseMe)
            return memo[key]

        # Start from the first coin, with a total of 0 and having used 0 coins so far.
        res = minCoinsFromIndex(0, 0, 0)

        # If our result is infinity, that means we never found a valid combination that reaches our target amount.
        # Otherwise, we can return the minimum number of coins we found.
        return -1 if res == float('inf') else res