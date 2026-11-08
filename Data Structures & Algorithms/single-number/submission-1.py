class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # So intuitively you might want to use maybe a set or some other approach to keep track of the duplicates
        # But there is a really clever way we can solve this problem without using extra memory.. Thanks to good ol bit manipulation
        # You see, there is a special bit operation XOR which basically compares two numbers bit by bit, and gives us a 1 only where the bits are different
        # Two important properties of XOR is that a number XORed with itself gives 0, and a number XORed with 0 gives back the same number
        # Another important property is that the calculations are commutative and associative, ie the order does not really matter
        # Meaning 0 ^ 4 ^ 1 ^ 2 ^ 1 ^ 2 is same as 0 ^ 4 ^ (1 ^ 1) ^ (2 ^ 2)
        # If you think about what this implies, it means if we just repeatedly store the result of XORing the elements in the array, our single element is the only thing that will not be cancelled out
        # Because the effects of all the duplicates will be XORed with themselves and turn to 0, and we will only be left with 0 ^ thesingledigit
        # So we can just return whatever we are left with after that calculation.

        res = 0

        for num in nums:
            # XOR the new element with whatever we have calculated so far, we expect the results to cancel out as explained above
            res ^= num # Same as previous solution, just shorthanded
        
        return res