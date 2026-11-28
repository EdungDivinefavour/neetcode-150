class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # The first thing to keep in mind is that nums[i] is the maximum we can jump from i, not a required jump. 
        # So we don't necessarily need to use the entire jump. We just want to know if we can reach there 
        
        # We can do this in a BottomUp DP-like way ie Instead of asking "can I reach the end from here?" for every index, let's think of it from the end.. 
        # At the last index, can we reach the end? Yes.. by just being here. So the last index is a "good" index

        # Now at the 2nd last index, can we reach the last? If our jump is >= the distance from us to the last, we can.
        # And that is the whole idea.. every index only needs to ask "can I reach the closest good index to my right?"
        # We don't need to ask about the good indexes further right, because if we can reach one of those, we can also reach the closer one.. we are allowed to jump shorter
        # If we can't reach the closest good index, then we are not good ourselves, so whoever is to our left now has one more step to cover to get to a good index
        # If we can reach it, we are good, and the next person on the left only needs one step to reach us
        # eg
        # [2, 1, 0, 3, 2, 1, 0]
        # [3, 0, 4, 0, 0, 0, 1]

        # dp[i] is to hold the distance from index i to the closest good index on its right (1 if i itself is good)
        # The extra spot I added at the end is for the base case so that the last index doesn't need any distance to reach the end so it always passes the check below
        dp = [0] * (len(nums)+1)

        for i in range(len(nums) -1, -1, -1):

            # Do we have enough to reach the closest good index? which is stored in the DP
            # # We have enough, so this will reset the distance.. the next guy on the left will only need one step to reach us(A valid person that can reach the end)
            if nums[i] >= dp[i+1]: dp[i] = 1 
            
            # We cannot reach the nearest guy who can reach the end from here, so the distance to the closest good index will grow by one for the next guy
            else: dp[i] = dp[i+1] + 1 

        # If index 0 is good, it means it can reach the end
        return dp[0] == 1