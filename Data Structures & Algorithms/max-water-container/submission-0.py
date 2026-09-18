class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # This is an interesting question because at first glance, given [1,7,2,5,4,7,3,6] 
        # you would think to multiply the two largest numbers eg 7 and 7 to get 49
        # But no :)
        # Remember we are looking for a container..so we have to 'also' account for the width
        # This means we have to strive to get as much height as possible.. definitely.......
        # Buuuuut we also have to get as much width as possible.

        # We can keep 2 pointers at both ends so we can start with the max width possible
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            # Also, we can/should be greedy about our pointers as much as possible
            # except we have good reason to move either one.. Basically we want to move whichever one that is the smaller of the two. So that we can potentially hit the next biggest height we can find.

            # Remember the container is only as useful as its shortest side's height
            height = min(heights[l], heights[r])
            width = r - l
            area = height * width

            # We are trying to get the maximum possible area so we can keep replacing the previous ones if we get a bigger area
            maxArea = max(maxArea, area)

            if heights[l] <= heights[r]: 
                l += 1
            else: 
                r -= 1
            
        return maxArea