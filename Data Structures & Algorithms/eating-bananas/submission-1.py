class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # We know for sure that at a minimum if we eat at a rate of 1 banana we will eventually finish all the bananas.
        # The problem is that we may not finish it in time
        # We also know that if we choose a big enough rate eg the max in the array, we will definitely eat through all the bananas in len(piles) time.
        # The problem with the second option is that this is the maximum eating rate, but the question wants the minimum rate.
        # So intuitively the next thing we might want to do is to try all rates from 1 to the the max rate, and then return the lowest one that allows us eat all in time

        # Notice that we are not searching the array at all here.. we are searching through every possible rate
        # And the array is only there to grade whichever rate we are currently trying

        for rate in range(1, max(piles) + 1):

            # To grade a rate, we can just go pile by pile and ask how many hours this rate needs to finish that pile
            # We use ceil because Koko doesn't move on to the next pile within the same hour.. so even 1 banana left over still costs us a whole hour
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)

            # Now that I think about it, we don't even need to update the min because we are going from lowest value upward, so the first value that allows us to eat all of them, is our guy
            if hours <= h: return rate

        return k


        



