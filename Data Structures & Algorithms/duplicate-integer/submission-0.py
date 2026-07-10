class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        A = set()

        for num in nums:
            if num in A: return True
            A.add(num)
        
        return False