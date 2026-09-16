class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # The brute force approach to solving this problem would be to do O(n^3) loop
        # Such that we compare i and j and k after entering the third loop but this will be suuuuper inefficient.
        
        # But we can make things a bit better by sorting first ie O(nlog(n)). 
        # The advantage that sorting gives to us is that we can do an O(n) first and inside that loop
        # We can then convert this problem to 2sum(input array is sorted)
        
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1 # Start from the element after i, since there's no need to also count i

            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                    continue
                
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                    continue

                result.add((nums[i], nums[l], nums[r]))
                r -= 1

        return [list(triplet) for triplet in result]
