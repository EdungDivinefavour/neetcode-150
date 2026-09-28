class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # The brute force approach here would be to try every pair of days ie O(n^2)
        # But if you think about it, you will notice that we don't need to try every pair
        # We only ever want to buy low and sell high, so we can walk forward with 2 pointers(as a sliding window)
        # such that l is the day we are buying on and r is the day we are thinking of selling on
        # Keeping r ahead of l is what stops us from selling before we bought

        l, r, maxProfit = 0, 1, 0

        while r < len(prices):
            # If today is cheaper than our buy day, there is no reason to keep the old buy day
            # Anything we could have sold to later, we can sell to from here for more
            if prices[l] > prices[r]: 
                l = r
            else:
                # Otherwise we can actually sell today, so check it against our best profit so far
                maxProfit = max(maxProfit, prices[r] - prices[l])
            
            r += 1

        return maxProfit