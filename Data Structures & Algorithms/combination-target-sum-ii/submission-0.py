class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # So this is basically the last combination sum problem with a couple of twists
        # We can only use every number once... and candidates can have duplicates, but we can't return the same combination twice
        # So for every number, we only have 2 choices.. we can either take it or we don't. So if we explore both choices for every number, we will see every combination possible

        # The problem is the duplicates though, eg given [1,2,1] and a target of 3
        # Index 0 and index 1 gives us [1,2].. and index 1 and index 2 gives us [2,1]. That is basically the same combination, but our approach will treat them as different
        output = set()
        def dfs(i, acc, total):

            # We landed exactly on the target so whatever we are holding is a valid combination
            if total == target:
                # We can store it as a tuple in a set, because a list cannot go in a set, and the set will ignore the repititions for us
                output.add(tuple(sorted(acc)))
                return
            
            # We have gone past the target so there is no point going any further. 
            # Every number in candidates is a positive number so the total will only ever go up from here
            # And if we have run out of elements then there is nothing left to decide on either
            if total > target or i == len(candidates): return



            # We can add me to the accumulator
            acc.append(candidates[i])
            
            # Then explore the world where I was added. Notice that we go to i+1 and not i, since we can only use a number once
            dfs(i+1, acc, total + candidates[i])

            # When we are done exploring that, we can remove me and explore the path where I wasn't added
            acc.pop()

            # Now we can hand the baton over to the next guy and let him repeat the same process
            dfs(i+1, acc, total)


        dfs(0, [], 0)
        return [list(t) for t in output]