class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # We can do better than our previous solution
        # If you think about it, you will notice that the whole reason we have 2 loops is
        # So we can hold the current temperature we are interested in, until we find something warmer
        # But the disadvantage of this is that during our search for a warmer temperature, we might
        # walk past the same element multiple times.

        # We can do better with a stack! That is a perfect way to keep track of the days that are
        # still waiting for a warmer temperature.

        stack = []
        
        # We can just start with a zeroed out array to account for temps without any warmer days.
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            # If we encounter any temperature that is warmer than the top of the stack,
            # then we have just found that day's warmer temperature,
            # so we no longer need to keep the top element in the stack anymore
            while stack and temp > stack[-1][0]:
                _, y = stack.pop()

                # So we can store at index y, the difference between the current i index and the index of whatever the top is... 
                # this basically gives us how long it took to get a warmer temperature
                result[y] = i - y

            # If we haven't found a warmer temperature yet, we just push that day to the stack
            # So that we can keep waiting for the next warmer day
            stack.append((temp, i))

        return result