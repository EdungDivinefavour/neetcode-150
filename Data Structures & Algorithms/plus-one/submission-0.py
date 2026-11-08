class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # When adding numbers on paper, we do it from the end to the start.
        # Since we were provided the numbers as an array, we can loop the array backwards!
        # So we go from back to front, and then add one... and if there is a carry, we keep track of that and use it in the next iteration
        # We can do that repeatedly until we get to the start of the array.. if there is a carry, we can just add 1 as a new element at the start of the array

        carry = 0
        out = [0] * len(digits)
        for i in range(len(digits) - 1, -1, -1):
            res = 0

            # For the last element, ie the first time we start the addition, we are adding 1
            if i == len(digits) - 1: 
                res = digits[i] + 1
            
            # Every other time, we are adding carry to the element
            else:
                res = digits[i] + carry
            
            # If after this addition, we get a value 10 or above, we need to store the modulo instead of the direct result
            # And then set carry to 1.. so that the next iteration knows that we had something to carry
            out[i] = res % 10
            carry = 1 if res >= 10 else 0
        
        # Return our computed result array so far if there is nothing to carry... else add carry to the start of the array so that [9,9,9] can give [1,0,0,0]
        return out if not carry else [carry] + out