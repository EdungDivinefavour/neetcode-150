class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}

        # We could choose to store the values and their indices first and then check
        # later if the complement exists in the map.

        # Alternatively, we could store the diffs and the indices of who they complement
        # then check later if the one they complement exists.

        # I'll be choosing the latter as best practise ie its best to compute at the time
        # of storing

        for i, num in enumerate(nums):
            diff = target - num

            if A.get(num) != None:
                return [ A[num], i]

            A[diff] = i
    