class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # We can optimize the brute force approach
        # There is a data structure that takes care of this.... A set!
        # A set cannot contain duplicates, so we can simply create a set from our original array
        # And if we end up with less items in the set than the original, then the array contained a duplicate

        A = set(nums)

        return len(A) != len(nums)      