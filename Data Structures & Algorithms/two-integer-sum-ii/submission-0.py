class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # A brute force solution would be to do an O(n^2) loop and check for each i and j.. just like in Two Sum 1
        # Aside that approach... I can already think of some other terrible ways to do it. 
        # But I think we can do better... What advantage does sorting give us?
        # We know for sure that the smaller numbers will be at the start and the bigger ones at the end
        # So we can be creative and use... two pointers

        # If we keep a pointer at the start and one at the end, we can sum the elements located at both pointer ends, 
        # If the sum we get is smaller than our target, we need a bigger sum, so we can move our smaller pointer forward  
        # If the sum is bigger than our target, we need a smaller sum, so we can move our bigger pointer backward
        # If the sum is neither bigger nor smaller... then we have our elements

        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
                continue
            
            if numbers[l] + numbers[r] > target:
                r -= 1
                continue
            
            return [l+1, r+1] # The array is 1-indexed so we can just add 1