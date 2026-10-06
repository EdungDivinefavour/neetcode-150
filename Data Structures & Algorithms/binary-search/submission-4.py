class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # In the upper bound approach, we are also trying to get the smallest range where our desired value might exist
        # But unlike in the lower bound where we keep asking "are you my guy or higher"?... In the upper bound approach, we ask "are you higher than my target"?, and keep shrinking until there is only one spot left.
        # Think of it this way... there is some range inside the array where our value is most likely to exist.
        # We want to keep shrinking that range again and again until we get to the first answer to that question

        l, r = 0, len(nums)

        while l < r:
            mid = l + (r - l)//2
            
            # Remember I am asking.. are you strictly higher than my target? If yes, move r to mid.
            # We don't move it past mid because mid might be the first one higher, we haven't checked anything to its left yet
            if nums[mid] > target:
                r = mid
            
            # if not, mid is our target or smaller, so it cannot be the first one higher. We can move l past it
            # And everything to the left of mid is even smaller, so they are all useless as well
            else:
                l = mid + 1
        
        # Notice because its an upper bound, l will land on the first thing higher than our target, which means our target would be the one just before it
        # First we check that l didn't land at 0, because then there is nothing before it and nothing was ever our target
        # Then that whatever is just before l is actually our target and not just the next smallest thing
        if l > 0 and nums[l-1] == target:
            return l - 1
        else:
            return -1