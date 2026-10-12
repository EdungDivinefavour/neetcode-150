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
            # Which means acc is a finished subset now and we can hand it over to out
            # We have to append a copy and not acc itself, because this time around we are reusing the same list the whole way through
            # so if we stored acc directly, everything in out would end up pointing at that one list
            if index == len(nums):
                out.append(acc[:])
                return

            # If you think about this, we don't really need to build a new array every time we want to explore a path
            # We can use the same array the whole time!.. and just undo whatever we did to it before we try the other path

            acc.append(nums[index]) # Add our current guy to the accumulator            
            dfs(index + 1, acc) # We should explore the path with the new element added to the array

            acc.pop() # We have to undo that decision to add it

            dfs(index + 1, acc) # Then we can explore path without this value

        # At the start we want to use the first element, and ofcourse we haven't accumulated anything yet
        dfs(0, [])
        return out