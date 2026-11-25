class Solution:
    def myPow(self, x: float, n: int) -> float:
        # The first thing that comes to mind is.. well, raising x to the power of n is just multiplying x by itself n times
        # So we can start with 1 and keep multiplying it by x, n times
        # We start with 1 and not x, because anything to the power of 0 is 1.. and if n is 0 the loop will never run, so we can just return whatever we started with

        # What about a negative n? x to the power of -2 is the same as 1 / (x * x)
        # So instead of multiplying by x each time, we divide by x each time, and we still do it abs(n) times
        res = 1
        for _ in range(abs(n)):
            if n > 0:
                res *= x
            else:
                res /= x

        return res