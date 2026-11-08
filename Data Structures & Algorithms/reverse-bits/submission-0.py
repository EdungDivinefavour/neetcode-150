class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for _ in range(32):
            # First we can shift everything in our result once to the left so we can create space by the right
            result = (result << 1) 
            
            # Then, we can take the last bit from n by doing (n&1).. and then add that to the empty space we just created
            result = result | (n & 1)

            # Then shift n to the right so that we can dispose of the bit we just added to our result.. This way our new rightmost bit will be the one that was once before it
            n >>= 1

        return result