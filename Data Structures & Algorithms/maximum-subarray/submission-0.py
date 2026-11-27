class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # The brute force approach here would be to try every possible subarray
        # But if you think about it, we don't really need to do that
        # We can walk through the array while keeping track of our current subarray's sum
        # If at any point that sum becomes negative, there is no reason to carry it forward
        # eg if our current sum is -3 and the next element is 5, we are better off starting from 5 itself than adding 5 to -3
        # This is essentially the idea behind Kadane's Algorithm

        maxSub, curSum = nums[0], 0
        for num in nums:
            # If our current subarray has a negative sum, discard it and start a new subarray from num
            if curSum < 0: curSum = 0
            curSum += num

            # Check if the sum of our current subarray is better than the best we have seen so far
            maxSub = max(maxSub, curSum)

        return maxSub