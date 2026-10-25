class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # There are a few ways we can go about this problem I think. One suboptimal solution would be using sorting, eg Given [2, 3, 6, 2, 4]
        # We could first sort the array to get [2, 2, 3, 4, 6] and then we can pop from the right, and do our comparisons to decide how smashing them will go
        stones.sort()

        while len(stones) > 1:
            x, y = stones.pop(), stones.pop()

            # If the two stones are the same weight, we don't need to do anything since we already popped them
            # If x is bigger than y, then we can append their diff to the array and sort it since it may mess up our existing sort
            if x > y:
                stones.append(x-y)
                stones.sort()

        # If we end up with just one element in the array, return it. If not return 0
        return 0 if not stones else stones[0]