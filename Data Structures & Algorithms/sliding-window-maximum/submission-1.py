class Solution:
        # NOTE: Our previous solution technically works but is inefficient at two things
        # 1. At removing the element in front and 2. At getting the max from the window
        # For 1, we don't want to use an array to store the window because we are always adding from the back and removing from the front
        # If that sounds like a queue's job to you, thats because it is what we need here.
        # We haven't solved problem 2 yet but let's see how we perform now
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # It's a good thing the question's title already tells us that it is a sliding window problem 
        # So I guess we don't have to think too much about what 'technique' to use : )
        # From what the question expects, we want to start out with a window of size k at the start
        # Then check what the max in that window is, slide right and repeat
        out, window = [], deque([])

        for r in range(len(nums)):
            window.append(nums[r])
            if r < k-1: continue # For the first 2, we just want to keep adding to the window
            
            # At this point I have enough to compare
            out.append(max(window))

            # Remove an element from the front
            window.popleft()

        return out

        