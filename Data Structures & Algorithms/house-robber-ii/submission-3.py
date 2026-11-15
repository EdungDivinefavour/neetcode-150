class Solution:
    def rob(self, nums: List[int]) -> int:
        # This is basically the last house robber problem with a small twist.. the houses are now in a circle
        # Which means the first house and the last house are now neighbors, so we can't rob both of them
        # So what do we do then? Well.. we can break it down into 2 simple cases
        # Either we don't rob the last house, so we only look at the first house up to the 2nd last
        # Or we don't rob the first house, so we only look at the 2nd house up to the last
        # In both of those cases, the first and last house can never be robbed together, so each one is just the same old house robber problem on a straight line
        # And whichever case gives us the bigger stash is our answer

        # If there is only one house, we can just rob it
        if len(nums) == 1: return nums[0]

        # This is the bottom up solution with 2 variables from the last problem, except now we can decide where to start and where to end
        def robHouses(start, end):
            # If we only have one house in our range, there is nothing else to choose from so we rob it
            if start == end: return nums[start]
            
            # We start from the end of our range and work backwards
            # two is the max we can get from the last house, which is just the house itself
            # one is the max we can get from the last two houses, which is whichever of them is bigger since we can't rob both
            one, two = max(nums[end], nums[end-1]), nums[end]

            # Then we loop from two steps back of wherever we wanted to end, since we already figured out the initial dp values of the last 2
            for i in range(end-2, start-1, -1):
                # Either we rob this house and add whatever we got from two houses ahead, or we skip it and take what we got from one house ahead
                temp = max(nums[i] + two, one)

                # Then we can shift everything over, same as the last problem
                two = one
                one = temp
            
            # By the time we get to start, one will hold the max we can rob from our entire range
            return one
        
        # Now we can try both cases and take whichever is bigger
        return max(
            robHouses(0, len(nums)-2), # Go from start of array to 2nd last
            robHouses(1, len(nums)-1) # Go from 2nd house of array to last
        )