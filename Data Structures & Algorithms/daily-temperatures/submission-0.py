class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # A very brute force approach to this problem would be
        # To iterate through the temperatures and for each i, iterate again from i+1 to the end until we find some other temperature that is warmer
        # Then we get the distance between i and wherever we found the warmer temperature.. and add that distance to the results array

        results = []

        l = 0
        while l < len(temperatures):
            r = l + 1

            # If we haven't seen any warmer temperatures, keep moving r forward
            while r < len(temperatures) and temperatures[r] <= temperatures[l]:
                r += 1
            
            # If we moved r too forward such that we went past the array, then nothing was bigger
            if r >= len(temperatures):
                results.append(0)
            
            # If we found a warmer temperature sooner
            else:
                results.append(r - l)
            l += 1

        return results