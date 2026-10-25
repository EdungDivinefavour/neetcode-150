class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # The lazy approach to this problem as you can imagine will be to sort the array and then return the kth element from behind

        nums.sort()
        return nums[-k]