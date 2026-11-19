class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # So for this question, the first thing we want to figure out is what makes a product big or small
        # If we multiply by a positive number, the product will get bigger. If we multiply by a 0, we lose everything we had built up so far
        # And if we multiply by a negative number, the sign will flip.. which means two negatives will cancel each other out and give us a positive again!
        
        # So if we look at any stretch of numbers with no zeros in it, we will only have two cases
        # If we have an even number of negatives in it, then the product of the whole stretch is positive and as big as it can get, so we just take all of it
        # If we have an odd number of negatives, we have to throw one of them out. The best way to do that is to cut off everything up to the first negative, or everything from the last negative onwards

        # Now think about what we are left with after that cutting.. it is either a prefix of the stretch or a suffix of the stretch
        # So if we just keep one running product going from the left and another one going from the right, one of them will always land on our best answer : )
        # We start res at nums[0] and not 0, because if nums is something like [-2], the answer is -2 and not 0
        n, res = len(nums), nums[0]
        prefix = suffix = 0

        for i in range(n):
            # Here prefix is our running product from the left and suffix is our running product from the right
            # The only catch is zeros.. once we hit a 0, our running product becomes 0 and everything after it would stay 0 forever
            # So whenever prefix or suffix is 0, we use 1 instead ie we start fresh from the next number, as if the zero was a wall
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)

            # Then we just keep track of the biggest one we have seen from either direction
            res = max(res, max(prefix, suffix))
        return res