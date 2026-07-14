class Solution:
    # Because we are returning the value and not the index
    # And we must do a loop within a loop since we need to
    # hold 3 nums at a time for comparison.... This presents
    # us with an advantage to sort the list since our worst case is O(n^2) anyway
    # Therefore this problem reduces to '2 sum when input array is sorted'
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = set()
        for i in range(len(nums)):
            # We don't need to set pointers from start to end
            # We can simply set the left pointer to the element after whatever index we're at
            # for more efficiency since we know for sure that the array is sorted
            l, r = i+1, len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    # Because we need the result array to be unique, we have to store the result
                    # in a set. But a standard set cannot hold lists.. so we improvise with a tuple
                    res.add((nums[i], nums[l], nums[r]))

                    # We need to advance the pointers just incase 'i' can still form another
                    # set of triplets
                    l += 1
                    r -= 1
                    
                    continue

        return list(list(res))