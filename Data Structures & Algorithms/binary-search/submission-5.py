class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # There is one more approach we can try.. Recursion!
        # While it is not the most efficient in this case because of the need for the call stack, it just feels so natural for this kind of problem where we want to repeatedly do the same thing

        def binarySearch(start, end) -> int:
            # At this point, we have shrunk the range down to nothing, so our guy was never in the array
            if start == end: return -1

            mid = start + (end - start)//2
            if nums[mid] < target:
                return binarySearch(mid+1, end)
            elif nums[mid] > target:
                return binarySearch(start, mid)
            else:
                return mid
            
        return binarySearch(0, len(nums))