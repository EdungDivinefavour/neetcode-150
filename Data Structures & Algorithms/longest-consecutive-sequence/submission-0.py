class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # A brute force-like approach to this problem would be to sort the array and then iterate through 
        # during this iteration, we can check if the difference between every element and its last, is not more than 1.      
        #This will give us our sequences.. However this will be an O(nlogn) at best because of the sorting and the question says to build an O(n) solution.

        # The thing sorting was really buying us was the ability to ask "whats next to me".
        # But you see, we dont need everything lined up in order for that, we just need to be able to ask
        # "is this particular number around?" and get an answer right away.. which is exactly what a set gives us.
        # So the plan is: We just dump everything into a set, then find the numbers that start a sequence, and count up from each of them

        maxLength, A = 0, set(nums)
        # I am iterating through A because A has already been deduplicated so if we initially had a lot of repitition, this will be waaaay more efficient than using len(nums)
        for num in A: 

            # Adding this for more efficiency, because if a smaller member of the sequence is in the set, 
            # We dont need to worry about me because we will eventually meet the guy at the start of the sequence who will help us count
            if num - 1 in A: continue

            # At this point, nothing is below me, so I am the bottom of the sequence and its my job to count it
            length = 1
            while num + length in A:
                length += 1
            
            maxLength = max(maxLength, length)
        
        return maxLength