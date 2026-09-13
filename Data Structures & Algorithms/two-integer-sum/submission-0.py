class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # The brute force approach to this would be
        # To iterate through each element in the array
        # For each element i, we iterate again through every element in the array
        # If we find any element j (except where i = j so we dont count i twice)... and those 2 elements that sums up to give target
        # Then we have found our pair and we can return i and j

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue

                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return [-1, -1]