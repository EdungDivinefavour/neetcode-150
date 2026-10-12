class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Unlike the subsets question where every element was either in or out, here we are allowed to use the same
        # element as many times as we want.. so we are not really asking if we have used an element or not
        # The question at every level is basically "what element do I add next" and this choice could come from any of the elements in the array

        # We will need to pass three things around.. a start to say which element we are allowed to begin picking from,
        # an accumulator to hold whatever we have picked up so far, and a total so we don't have to keep summing the accumulator array all over again
        
        out = []
        def dfs(start, acc, total):
            # If we have gone over the target, there is no point of going any deeper down this path
            if total > target: return

            # If we landed exactly on the target, the accumulator is a valid combination so we can hand it over to out
            if total == target:
                out.append(acc[:])
                return

            # At every level, I want to explore adding the first guy, or the second guy, or the third guy etc etc... 
            # Doe that sound like a loop to you? Yep! Thats why we have one..
            # But notice we are starting from start and not from 0.. without that we would be allowed to go backwards
            # and pick up something we had already moved past, which is how we can end up with both [2,3] and [3,2]
            # Also notice we are handing down i and not i + 1, because we are still allowed to pick this same element again
            # ie that is what lets [2,2,5] happen
            for i in range(start, len(nums)):
                dfs(
                    i,
                    [*acc, nums[i]],  
                    total + nums[i]
                )

        dfs(0, [], 0)
        return out