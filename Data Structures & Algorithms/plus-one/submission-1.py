class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Compared to the last solution, I see a ton of improvements we can make.

        # We can simply start with a carry of 1!... Since we are anyway doing the same addition.. This way, we don't need a special condition for the last element
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            # Also, think about it.. if we run out of carry, is there any need to continue iterating through the rest of the array? No!
            # So once carry is exhaused... we can just break out of this for loop
            if not carry: break
            
            res = digits[i] + carry
            
            # If after this addition, we get a value 10 or above, we need to store the modulo instead of the direct result
            # And then set carry to 1.. so that the next iteration knows that we had something to carry
            # We also don't need a special out array like in the last solution, we can modify the existing array in place!
            digits[i] = res % 10
            carry = 1 if res >= 10 else 0
        
        # Return our computed result array so far if there is nothing to carry... else add carry to the start of the array so that [9,9,9] can give [1,0,0,0]
        return digits if not carry else [carry] + digits