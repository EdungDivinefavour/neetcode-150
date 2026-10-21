class Solution:
        # NOTE: Our previous solution technically works but is inefficient at two things
        # 1. At removing the element in front and 2. At getting the max from the window
        # For 1, we don't want to use an array to store the window because we are always adding from the back and removing from the front
        # If that sounds like a queue's job to you, thats because it is what we need here.
        # Now for problem 2, instead of keeping everything, we only keep the numbers that still have a chance of being the max
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # It's a good thing the question's title already tells us that it is a sliding window problem 
        # So I guess we don't have to think too much about what 'technique' to use : )
        # From what the question expects, we want to start out with a window of size k at the start
        # Then check what the max in that window is, slide right and repeat
        # Note that our queue is not the window.. the window is just the last k numbers in nums, the queue only holds the guys that could still become the max
        out, queue = [], deque()

        for r in range(len(nums)):
            # I think there is a trick we can use here whenever we want to add a new number to the queue, 
            # We can check if its bigger than what is currently at the back of the queue
            # If it is, those guys can never be the max again because the new number is bigger and will stay in the window longer than them, so we can kick them out
            # This way, the front will always hold the max element
            # eg if I have 5 4 3 2 .... and then 10 comes, I want to remove the rightmost guys
            while queue and nums[r] > queue[-1]:
                queue.pop()
            queue.append(nums[r])

            # For the first k-1, our window isn't complete yet, so we just keep adding
            if r < k-1: continue 
        
            # At this point I have a full window, and the max is at the front of the queue
            out.append(queue[0])

            # Now we can slide, so basically nums[r-k+1] is the guy about to leave the window
            # If he is at the front of our queue, he is expired so we remove him
            # If he isn't, it means a bigger number already removed him from the back earlier, so no need to do anything
            if queue[0] == nums[r-k+1]: queue.popleft()

        return out