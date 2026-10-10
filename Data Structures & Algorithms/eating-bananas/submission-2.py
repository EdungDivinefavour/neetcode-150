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
        k, l, r = max(piles), 1, max(piles)
        while l <= r:
            mid = l + (r - l)//2

            # To grade a rate, we can just go pile by pile and ask how many hours this rate needs to finish that pile
            # We use ceil because Koko doesn't move on to the next pile within the same hour.. so even 1 banana left over still costs us a whole hour
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            # In the brute force we didn't need to keep track of any min, because we were going from the lowest value upward
            # so the first value that allowed us to eat all of them was our guy
            # But that doesn't hold here because binary search doesn't go in order, and since we do r = mid - 1
            # we end up throwing away the spot that worked. So we have to store it in k before we lose it
            if hours <= h: 
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1

        return k