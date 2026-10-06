class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # In the lower bound approach, we are trying to get the smallest range where our desired value might exist
        # Unlike the traditional binary search, where we keep asking "is this it"?... In the lower bound approach, we never ask "is this it?" inside the loop.
        # We ask "are you atleast target or higher", and keep shrinking until there is only one spot left.
        # Think of it this way... there is some range inside the array where our value is most likely to exist.
        # We want to keep shrinking that range again and again until we get to the first answer to that question

        # r starts at len(nums) and not len(nums) - 1, because our answer can be a spot past the last element
        # ie if target is bigger than everything, every element will say no
        l, r = 0, len(nums)

        while l < r:
            mid = l + (r - l)//2
            
            # Remember I am asking.. are you atleast target or higher? If yes, move r to mid.
            # We don't want to move it past mid because mid may be our value since we asked "are you mid or higher"
            # Everything to the right of mid is a potential yes too, but we don't know yet so we preserve them for now
            if nums[mid] >= target:
                r = mid
            
            # if not, we can move l past mid. We don't need to preserve the element at mid at this point since we know it cannot possibly be our value
            # And everything to the left of mid is even smaller, so they are all useless as well
            else:
                l = mid + 1
        
        # The loop only tells us where target would go, not whether it is actually there.. so we need to check once at the end
        # First that l didn't go off the end of the array, which will happen when nothing was big enough
        # Then that whatever we landed on is actually our target and not just the next biggest thing
        if l < len(nums) and nums[l] == target: 
            return l
        else:
            return -1