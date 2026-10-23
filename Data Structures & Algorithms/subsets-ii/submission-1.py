class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # So the last solution passed, but I wonder if we can avoid duplicates during the decision making itself?
        # How would [2,1] know to be rejected if we already saw [1,2] first
        # I think if we sort the input array first, we would have all the duplicates close to each other
        # And it is those initial duplicates that cause our output array to contain duplicates
        nums.sort()

        
        output = []
        def dfs(i, accumulator):
            # At this point we can't possibly have a valid index and also we would have considered every element
            if i >= len(nums):
                output.append(accumulator[:])
                return

            # Add me to accumulator
            accumulator.append(nums[i])

            # Pass the baton over to the next guy to explore the subsets where I existed
            dfs(i+1, accumulator)

            # Remove me from the accumulator
            accumulator.pop()

            # Now we have explored everything with me inside, if the element beside me is same as me, skip that..
            # Keep skipping until we have something genuinely different that we can go exploring
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            # Pass the baton over to the next guy to explore the subsets where I didn't exist
            dfs(i+1, accumulator)

        dfs(0, [])
        return output