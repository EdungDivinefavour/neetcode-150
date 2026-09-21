class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # There are several ways to go about this... For one we can get the product of the array and then store the result of dividing that product by each element.
        # But the question asks to not use the division operation... So what can we do now
        # Well, we can use a prefix and suffix array.
        # A prefix array stores cumulative information(sum/product etc depending on our needs) from start to a given index
        # A suffix array stores cumulative information(sum/product etc depending on our needs) from a given index to the end
        # This means that, for us to get the product of everything except itself, we can simply multiply everything before it(ie prefix) with everything after(suffix)
        prefix = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0: continue # There is nothing before the first element so there is nothing to do here

            prefix[i] = nums[i - 1] * prefix[i - 1]

        
        suffix = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1: continue # There is nothing after the first element so there is nothing to do here
            
            suffix[i] = nums[i + 1] * suffix[i + 1]
        
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]

        return result