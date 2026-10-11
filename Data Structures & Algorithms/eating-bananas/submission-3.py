class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # We know for sure that at a minimum if we eat at a rate of 1 banana we will eventually finish all the bananas.
        # The problem is that we may not finish it in time
        # We also know that if we choose a big enough rate eg the max in the array, we will definitely eat through all the bananas in len(piles) time.
        # The problem with the second option is that this is the maximum eating rate, but the question wants the minimum rate.
        # So intuitively the next thing we might want to do is to try all rates from 1 to the the max rate, and then return the lowest one that allows us eat all in time

        # Notice that we are not searching the array at all here.. we are searching through every possible rate
        # And the array is only there to grade whichever rate we are currently trying


        # So instead of searching all the way from 1 to whoknowswhat, we can use binary search!
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l)//2

            # To grade a rate, we can just go pile by pile and ask how many hours this rate needs to finish that pile
            # We use ceil because Koko doesn't move on to the next pile within the same hour.. so even 1 banana left over still costs us a whole hour
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            # In the lower bound approach, we are asking a question that is no for a while and then yes forever, and we want the first yes
            # Here the question is "can I finish in time at this rate", and the answers look like this
            # [ 1  2  3  4  5  6  7  8  9  10  11]
            # [ no no no no no no yes yes yes yes yes]
            # Notice the direction is flipped from the usual sorted array case.. there the values climb as we move right,
            # but here the hours actually drop as the rate climbs, so our yes is hours <= h and not hours >= h
            if hours <= h: 
                # This rate works, so it is either our guy or a rate after our guy. Either way nothing to the right of it matters
                r = mid
            else:
                # This rate is too slow, and so is everything below it
                l = mid + 1

        return l