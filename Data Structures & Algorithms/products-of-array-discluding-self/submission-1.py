class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # In our last solution, we stored the cummulative product of everything before a given element. But did you notice any redundancy?
        # For prefix, once we got the most recent product... we no longer had need for the other things in the array... same for suffix
        # So.. did we even need an array at all? No.. we didn't
        # We could just keep some variable that would store the most recent product and use that in our calculation
        # Since ultimately we want to multiply the outcome of prefix and suffix array, but we no longer have the said array
        # We could just initially keep track of the outcome of multiplying by prefix, inside of the result array
        # And then multiply our result array by suffix

        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            if i == 0: continue # There is nothing before the first element so there is nothing to do here

            result[i] *= nums[i - 1] * prefix
            prefix = result[i] # Update prefix to hold the forward product so far

        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1: continue # There is nothing after the first element so there is nothing to do here
            
            result[i] *= nums[i + 1] * suffix
            suffix = nums[i + 1] * suffix # Update suffix to hold the backward product so far

        return result