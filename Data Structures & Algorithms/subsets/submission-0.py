class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # A subset is just any combination of the elements, and that includes the empty one and the full array itself
        # Now for every element in the array we really only have two choices.. either it is in the subset or it isn't
        # So if we take those two choices at every single element, we will end up covering every possible subset
        # ie with [1,2,3] we decide on 1, then on 2, then on 3, and each of those decisions will split into two more paths

        # This feels like recursion because once we have decided on the first element, whatever is left over is just a smaller version of the same problem 
        # ie decide on the rest of the array.... So each call will only deal with one element, and then hand the rest down to the next call

        # We will need to pass two things around.. an index to say which element we are deciding on right now,
        # and an accumulator to hold whatever we have picked up so far on this particular path
        
        out = []
        def dfs(index, acc):
            # This is our base case. The index has gone past the end of the array so there is nothing left to decide on
            # Which means acc is a finished subset now and we can hand it over to out
            if index == len(nums):
                out.append(acc[:])
                return

            # Each of the two paths will be handed their own list, so neither of them will be able to mess with what the other one is holding
            # The one that takes the element will get a brand new list with it added on the end,
            # and the one that skips it will just carry on with whatever acc we already had
            
            dfs(index + 1, [*acc, nums[index]]) # We should explore the path with the new element added to the array
            dfs(index + 1, acc) # Then we can explore path without this value

        # At the start we want to use the first element, and ofcourse we haven't accumulated anything yet
        dfs(0, [])
        return out