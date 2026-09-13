class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # A better way to handle this would be using hashsets!
        # We know that for each el in nums, if it is part of our chosen pair, then its complement has to exist in the array too
        # eg if 3 is in our chosen pair, then 4 has to exist in the array
        # With this in mind, we can simply store each element's complement whenever we see the element
        # And if we ever encounter that complement during our iteration, we have found our pair

        A = {}
        for i in range(len(nums)):
            el = nums[i]

            if A.get(el) != None: # For a given element, if we tried to retrieve it from the map and it exists.. this means someone must have previously stored it as a complement
                return [ A[el], i ] # Return the index of sibling who stored it.... and its own index

            complement = target - el # Get the complement
            A[complement] = i # Store that complement in the map... and set its value to the index of the sibling who stored it
        
        return [-1, -1]