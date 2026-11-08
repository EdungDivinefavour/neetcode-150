class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # I think we can do a bit of clever math here because think about this...
        # If we knew the sum of every number in the range from 0 to n inclusive, 
        # This means that subtracting the array's sum from the range's sum will tell us the missing number!

        rangeSum = sum(range(len(nums)+1))
        arraySum = sum(nums)

        return rangeSum - arraySum