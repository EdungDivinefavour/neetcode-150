class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # So for this question, we want the length of the longest increasing subsequence.. and remember that a subsequence doesn't have to be next to each other in the array, we can skip numbers as long as the order is kept
        # The first thing we want to figure out is, how do we break this into smaller problems?
        # Well.. if we pick some index i as the start of our sequence, the next number we pick can be any number after it that is bigger
        # And from every one of those bigger numbers, we are basically asking the same question again.. what is the longest sequence we can get if we start from here?
        # Since we have no idea which index is the best place to start from, we can simply try every single index and keep the biggest result

        # Now if you think about it, doing just that will have us recomputing a lot of things, eg given [1,2,3,4]
        # From index 0 we go to 3, then from 1 we go to 3 again and then from 2.. so we keep redoing the same work for index 3
        # But the longest sequence starting from a given index will never change regardless of how we got to that index
        # So once we compute it, we can simply save it in memo and return it whenever we are asked for that index again : )
        memo = {}

        def goThroughPossibilities(i):
            # If we already computed the longest sequence starting from this index, we can just return that value
            if i in memo: return memo[i]

            # A number on its own is already a sequence of length 1
            maxSeq = 1

            # Go through every possibility from here
            for j in range(i + 1, len(nums)):

                # We are only interested in numbers bigger than us, because the sequence has to keep increasing
                # If we find one, we count ourselves + the longest sequence we can get starting from that number
                if nums[j] > nums[i]:
                    maxSeq = max(
                        maxSeq,
                        1 + goThroughPossibilities(j)
                    )

            memo[i] = maxSeq
            return memo[i]

        # Ofcourse we don't know where the best sequence starts, so we try every index and keep the biggest
        return max(goThroughPossibilities(i) for i in range(len(nums)))