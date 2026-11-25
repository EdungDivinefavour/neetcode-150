class Solution:
    # Oops I should have memoized the last solution : ) That will be fixed below

    def canPartition(self, nums: List[int]) -> bool:
        # My initial thoughts were in this direction 
        # ========================
        # Since we are dealing with subsets, why not just generate every possible subset using our usual take or not take approach? Then compare every subset with every other subset to see if we can find two subsets whose sums are equal.
        # Or even better, we can store the sums of all the generated subsets and simply check if we have any duplicate sums.
        # But this will fail when we have something like [1, 1, 3]. We can generate two subsets [1] and [1] with equal sums, but that doesn't mean we have successfully partitioned the array because we still have 3 left over.
        # So we would also need to ensure that the two subsets don't share any elements (by index) and that between them, they contain every element in the original array.
        # =================================================================

        # The main thing I missed until I saw in a solution was that since we are trying to divide the array into two subsets such that sum(everything in one) == sum(everything in the other), this tells us something very interesting.
        # Each subset will have to sum up to exactly half of the total sum of nums.. because the only way we are getting two equal sums for any total is if that total was neatly divided into two.
        # This means we don't actually have to compare every subset with every other subset or worry about overlapping elements : )

        # Because we want two equal halves, we just have to ask.. can we generate a subset whose sum is equal to half of the array's sum?
        # If yes, we found our answer! Everything we didn't include in that subset will automatically make up the other half.
        # Also if the total is odd, HALF_SUM will have a .5 in it, and no subset can ever sum up to that.. so we get False without needing a special condition for it
        LEN, HALF_SUM = len(nums), sum(nums)/2
        memo = {}

        def subsetSum(i, comb):
            # We need to memoize by both i and comb because the answer from here depends on those two things.. where we are in the array, and how much we have collected so far
            # Different paths can land on the same spot, eg given [1, 1, 2] taking the first 1 and skipping the second gives us (i=2, comb=1), and so does skipping the first and taking the second
            # Since the rest of the work from there will be exactly the same, we can save it and reuse it : )
            if (i, comb) in memo: return memo[(i, comb)]

            # There is nothing left to generate from this branch, so we can check if the sum of the subset we generated so far is exactly half.
            if i == LEN: return comb == HALF_SUM

            # Either we include the current element in our subset or we exclude it. If either of those decisions generates a valid subset, we return True.
            branchResult = subsetSum(i+1, comb+nums[i]) or subsetSum(i+1, comb)
            
            memo[(i, comb)] = branchResult
            return memo[(i, comb)]

        return subsetSum(0, 0)