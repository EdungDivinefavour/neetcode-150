class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # It's a good thing the question's title already tells us that it is a sliding window problem 
        # So I guess we don't have to think too much about what 'technique' to use : )
        # From what the question expects, we want to start out with a window of size k at the start
        # Then check what the max in that window is, slide right and repeat
        # The problem comes when we want to 'slide'.. If you think about this, what does that mean for our array if we use that for our window?
        # We would have to reposition everything after removing the first element

        out, window = [], []

        for r in range(len(nums)):
            window.append(nums[r])
            if r < k-1: continue # For the first 2, we just want to keep adding to the window
            
            # At this point I have enough to compare
            out.append(max(window))

            # Remove an element 
            window.pop(0)

        return out

        