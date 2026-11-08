class Solution:
    def hammingWeight(self, n: int) -> int:
        # The laziest way to solve this problem will be as follows : )
        binaryString = str(bin(n)) # First we convert the number to its binary form

        # Then count the number of 1s in the string
        return binaryString.count('1')