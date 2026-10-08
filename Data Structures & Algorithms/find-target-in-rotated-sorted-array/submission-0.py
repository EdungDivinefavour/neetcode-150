class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # A rotated sorted array is really two sorted sections together, and the only thing standing between us
        # and a normal binary search is that we dont know where one stops and the other starts
        # So we can just find that inflection spot first, and then we can do a regular binary search on whichever section our target belongs to.

        # This first part is the findMin question all over again.. we are looking for the first element of the small group
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] <= nums[r]: # We are surely in the smaller section
                r = mid
            else: # We are in the bigger section
                l = mid + 1
        minIndex = l
        
        # Now that i know the inflection point ie where l is, I basically have 2 confirmed sorted sections and where they start and stop
        # Our target could be in the left or right end
        
        l, r = 0, len(nums) - 1

        # The small section is basically from minIndex to the very end of the array
        if nums[minIndex] <= target <= nums[r]: # The number is in the smaller range
            l = minIndex
        
        # Otherwise our target is either in the big section or nowhere at all, so we can cut off everything from minIndex onwards
        else:
            r = minIndex - 1

        # From here on its a plain old binary search, because whichever section we picked is properly sorted
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid

        return -1