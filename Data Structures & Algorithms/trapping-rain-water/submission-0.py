class Solution:
    def trap(self, height: List[int]) -> int:
        # There are several ways I think we can solve this problem
        # I don't want to image what the brute force version would be like : )
        # But one approach that will cost O(n) time and space.... that I can think of is as follows:

        # You see, the thing that decides how much water I have in any cell is the shorter of the two tallest walls around it
        # So at each cell we need to know two things.. the tallest thing to my left and the tallest thing to my right
        # Walking forward only ever gives us the left one, because the right side hasn't happened yet
        # So we just walk it twice(front and back) and write both down before we start counting anything


        # Walk forward and store at each cell, the largest we have seen so far going forward
        tallestToLeft, maxL = [0] * len(height), 0
        for i in range(len(height)):
            maxL = max(maxL, height[i])
            tallestToLeft[i] = maxL
        
        # Then we do the same for the back.. same idea, just coming from the other end
        tallestToRight, maxR = [0] * len(height), 0
        for i in range(len(height) -1 , -1, -1):
            maxR = max(maxR, height[i])
            tallestToRight[i] = maxR
        
        # Now at each cell we know how much water we can trap, because we know the tallest to its left and the tallest to its right
        result = 0
        for i in range(len(height)):
            # We take the minimum between the two walls since the shorter one is what limits us.. water would just spill over that side otherwise
            cap = min(tallestToLeft[i], tallestToRight[i])

            # Then we subtract the cell's own height from that, since the bar itself is taking up space that water cant
            # No need to worry about this going negative, because our forward walk included the cell itself,
            # so the cap can never end up shorter than the cell
            result += (cap - height[i])

        return result
