class Solution:
    def trap(self, height: List[int]) -> int:
        # Our last solution is totally valid... we could stop there if we wanted
        # Or we can have some more fun
        # If we keep two pointers, and then we see that one of them is smaller than the other, is there any fact we are absolutely certain of at that poiint?
        # We are certain that we already have our cap ie the smaller one between the two.... so we can consider it the maximum from that side that we have seen so far
        # The reason is that whatever is hiding between the two pointers cant lower the other side's max.. that side already has something taller than us ontop of it, and a max will only ever grow. 
        # So the shorter side's own max is what becomes our cap and we already know that number exactly. 
        # The taller side cant say the same thing, so it just waits for its turn

        # So we can keep two pointers, one at the start and one at the end
        l, r = 0, len(height) - 1

        # Similarly we can start out with our max per side as 0
        maxL, maxR = 0, 0

        result = 0
        while l < r:
            # We are updating both sides even though we will only use one of them this round.. we dont know yet which one we need,
            # and the unused really doesn't lose anything since a max only increases and that same height gets folded in again when its turn comes
            maxL, maxR = max(maxL, height[l]), max(maxR, height[r])

            # Whoever is standing on the shorter bar is the one whose answer is settled, so it fetches us some water and step forward
            if height[l] < height[r]:
                # To fetch water at a cell, we can simply subtract the cap between the l and r... ie the shorter one
                # and then subtract that from my height
                result += (maxL - height[l])
                l += 1
            else:
                result += (maxR - height[r])
                r -= 1

        return result