class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # This is almost the same as the subsets question, except that here we are allowed to use the same element
        # as many times as we want. So instead of "am I in or out", the decision is "do I take another me or not"
        
        output = []
        def dfs(i, acc, total):
            # We have gone past the target so there is no point going any further. 
            # Every number in nums is a positive number so the total will only ever go up from here
            # And if we have run out of elements then there is nothing left to decide on either
            if total > target or i == len(nums): return

            # We landed exactly on the target so whatever we are holding is a valid combination
            if total == target:
                output.append(acc[:])
                return

            # We can add me to the accumulator
            acc.append(nums[i])
            
            # Then explore the world where I was added. This will keep on adding me again and again and again btw
            # That is how we will end up with something like [2,2,5]
            dfs(i, acc, total + nums[i])

            # When we are done exploring that, we can remove me and explore the path where I wasn't added
            acc.pop()

            # Now we can hand the baton over to the next guy and let him repeat the same process
            dfs(i+1, acc, total)


        dfs(0, [], 0)
        return output