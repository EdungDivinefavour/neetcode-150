class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # A permutation is us trying to use every single element, and the only thing that changes is the order
        # So unlike subsets where we either pick something or not, in this question everybody is going in
        # The question at each level is basically... which one of the ones we haven't used yet do we put next
        # That is a different number of options depending on how far down we are, so we need a for loop
        
        output = []

        # We can keep a set of whoever we have already used on this path, so we don't put the same guy down twice
        # The question says the numbers are all different so a set of the values is enough for us here
        used = set()
        
        def dfs(acc) -> None:
            # We have used up everybody, so acc is a complete permutation
            if len(acc) == len(nums):
                output.append(list(acc))
                return

            for num in nums:
                # This number is already somewhere behind us on this path so we can skip him
                if num in used: continue

                # Then let's add me to the accumulator
                acc.append(num)
                used.add(num)
                
                # And then explore path with me added
                dfs(acc)

                # Remove me
                # And also free me up from the used set, otherwise the other branches would think I am still taken
                acc.pop()
                used.remove(num)
                
        dfs([])
        return output