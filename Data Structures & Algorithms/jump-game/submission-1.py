class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Notice anything with the last solution?
        # In the entire DP array we were only updating the value of our closest neighbor based on if he could reach the end or not
        # Similarly we were only performing our checks with the same closest neighbor so why do we need an entire array? We don't!
        # All we need is one variable that holds the distance from us to the closest good index on our right

        need = 0

        for i in range(len(nums) -1, -1, -1):
            # Do we have enough distance to reach the closest good index? That distance is what we are storing in need
            # If we do, we are good ourselves, so this will reset the distance.. the next guy on the left will only need one step to reach us (a valid person that can reach the end)
            if nums[i] >= need: need = 1 
            
            # We cannot reach the nearest guy who can reach the end from here, so the distance to the closest good index will grow by one for the next guy
            else: need += 1 

        # If index 0 is good, it means it can reach the end
        return need == 1