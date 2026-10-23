class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # My first thought is to do the same subset problem approach but instead to use a set to hold the outputs so far
        # I imagine this is not a very efficient solution as ontop of my O(n*2^n), I am still doing an O(nlogn) for insertions.
        # I am sorting because thats how two tuples (1,2) and (2,1) will be considered same in a set
        # Anyway, I will iterate on it.. Just looking to see how this one goes
        
        output = set()
        def dfs(i, accumulator):
            # At this point we can't possibly have a valid index and also we would have considered every element
            if i >= len(nums):
                # Then sort the list
                output.add(tuple(sorted(accumulator[:])))
                return

            # Add me to accumulator
            accumulator.append(nums[i])

            # Pass the baton over to the next guy to explore the subsets where I existed
            dfs(i+1, accumulator)

            # Remove me from the accumulator
            accumulator.pop()

            # Pass the baton over to the next guy to explore the subsets where I didn't exist
            dfs(i+1, accumulator)

        dfs(0, [])
        return list(output)