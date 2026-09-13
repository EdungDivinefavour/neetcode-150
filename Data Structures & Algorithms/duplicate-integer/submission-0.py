class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # The brute force approach
        # Loop through each element in the array and for each element
        # Loop again to see if the ith element exists at some other position other than i
        # We exclude i from the check so that we don't end up checking each element against itself

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue

                if nums[i] == nums [j]: return True
        
        return False