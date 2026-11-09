class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # So the first thing we do is sort the candidates. This will put all the duplicates right next to each other
        # The importance of this is will come in later when we want to skip over the repeated numbers in one go
        candidates.sort()

        # The previous solution worked but ofcourse was very inefficient... because we were exploring the exact same combination again and again through different indices
        # And we only discarded the repeats at the very end using a set, after the dfs had already done aaaaaall the work to build them
        # So this time, we want to make sure we never go down a path that is going to give us a repitition in the first place

        output = []
        def dfs(i, comb, total):
            # We check the target first because if we just took the last element, i may be out of bounds at the same time that we hit the target
            # If we checked i first, we would return early and never record a valid combination
            if total == target:
                output.append(comb[:])
                return
                
            if total > target or i >= len(candidates): return

            
            # We can add me to the combination
            comb.append(candidates[i])

            # Then explore the world where I was added. We go to i+1 and not i, because every number can only be used once
            # Notice that if the next guy is a duplicate of me, he can still be taken in this world.. so [1,1,6] is still reachable
            dfs(i+1, comb, total+candidates[i])

            # Now we want to explore the world where I wasn't added
            # But if I wasn't added, then none of my duplicates should be the one to take my place either, because that would give us the same combinations we just explored
            # Since the array is sorted, all my duplicates are right next to me, so we can skip over every one of them
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            comb.pop()

            # Now we can hand the baton over to the first guy that is different from me
            dfs(i+1, comb, total)
        
        dfs(0, [], 0)
        return output