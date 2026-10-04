class Solution:
    def findMin(self, nums: List[int]) -> int:
        # A rotated sorted array is really just two mini sorted chunks, and the minimum being right at the start of the second array
        # So we dont have to scan everything, we can keep halving the array as long as we can tell which half the minimum is hiding in

        l, r = 0, len(nums) - 1

        # Note that we are using l < r and not l <= r, because we are not looking for some target value that may or may not exist
        # The minimum is definitely inside of the array somewhere, so we can just keep shrinking the array until the two pointers land on it
        while l < r:
            mid = l + (r - l)//2

            # We are comparing against the right end instead of the left, because the right end is the one that tells us something about where the min is.
            # If mid is bigger than whatever is at r, then mid is somewhere in that first section, which means the flip
            # happens somewhere after it.. so the minimum cannot be mid or anything before it
            if nums[mid] > nums[r]:
                l = mid + 1

            # Otherwise mid is already in the second section, so the minimum is mid itself or something to its left.
            # We don't want to move r past mid ie mid - 1, since mid might be the answer
            else:
                r = mid
        
        # The pointers have collapsed onto one spot and thats our guy!
        return nums[l]