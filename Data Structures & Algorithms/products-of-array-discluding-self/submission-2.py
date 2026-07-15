class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution 1 using division operation
        total = 1
        zeroes = 0
        
        for num in nums:
            if num == 0:
                zeroes += 1
                continue
            total *= num

        res = [0] * len(nums)

        # If its all zeroes, just return the empty results array
        if zeroes > 1: return res

        for i, num in enumerate(nums):
            if zeroes:
                if num == 0:
                    res[i] = total
                else:
                    continue
            else:
                res[i] = total // num
                
        return res