class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Another way we can think about this problem is as follows... At each element, we have just 2 choices.. we either use it or we don't use it
        # If we explore both choices for every number, we will see every possible subsequence and we can keep the longest one that is increasing
        # To know if a number can be used, we only need to remember the biggest number we have used so far, which is why we are passing maxSoFar along

        # The problem with doing just that is that we end up recomputing a lot of things, eg given [1,2,3,4]
        # We can reach index 3 with maxSoFar = 2 by skipping 1... and also by skipping 2, and then again by using both
        # But the longest sequence we can get from index 3 onwards depends only on where we are (i) and what maxSoFar is, and it will never change regardless of how we got there
        # So once we compute it, we can simply save it in memo and return it whenever we are asked for that same i and maxSoFar again : )
        memo = {}

        LEN = len(nums)
        def goThroughPossibilities(i, maxSoFar):
            if i == LEN: return 0

            # If we already computed the answer for this exact i and maxSoFar, we can just return that value
            if (i, maxSoFar) in memo: return memo[(i, maxSoFar)]

            useMe = 0

            # if the next element is greater, then we want keep going and counting as we go
            if nums[i] > maxSoFar:
                useMe += 1 + goThroughPossibilities(i+1, nums[i])

            # Or we can skip it and just pass the baton over to the next element
            dontUseMe = goThroughPossibilities(i+1, maxSoFar)

            # Ofcourse we have to save whatever we computed before returning it, or there would be nothing for the next call to find
            memo[(i, maxSoFar)] = max(useMe, dontUseMe)

            return memo[(i, maxSoFar)]


        return goThroughPossibilities(0, float('-inf'))