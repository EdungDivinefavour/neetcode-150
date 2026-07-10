class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}

        # We could choose to store the values and their indices first and then check
        # later if the complement exists in the map.

        for i, num in enumerate(nums):
            diff = target - num

            if A.get(diff) != None:
                return [ A[diff], i ]

            A[num] = i
        
        return [-1, -1]