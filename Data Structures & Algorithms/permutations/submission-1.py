class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # A permutation is us trying to use every single element, and the only thing that changes is the order
        # So unlike subsets where we either pick something or not, in this question everybody is going in
        # The question at each level is basically... which one of the ones we haven't used yet do we put next
        # That is a different number of options depending on how far down we are, so we need a for loop
        
        output = []

        def dfs(acc, used) -> None:
            # We have used up everybody, so acc is a complete permutation
            if len(acc) == len(nums):
                output.append(list(acc))
                return

            for num in nums:
                # This number is already somewhere behind us on this path so we can skip him
                # Btw used contains exactly the same thing as acc.. The only reason why we pass it down alongside acc is because of the set's O(1) lookup time.
                # Since we are trying to ask whether the new element is inside what we have compiled so far
                if num in used: continue

                # Then let's add me to the accumulator
                acc.append(num)
                used.add(num)
                
                # And then explore path with me added
                dfs(acc, used)

                # Remove me
                # And also free me up from the used set, otherwise the other branches would think I am still taken
                # These two should always move together, because 'used' is just a faster copy of acc. If one of them ever goes out of sync with the other, we will have a bug
                acc.pop()
                used.remove(num)
                
        dfs([], set())
        return output