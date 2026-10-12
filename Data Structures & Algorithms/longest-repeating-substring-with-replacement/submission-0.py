class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # This looks like a sliding window problem.... For a sliding window, we want to maintain some truth the entire time 
        # The truth I want to maintain is that I only have the same char in my window
        # If I encounter a new character, it is still ok aslong as I still have Ks left
        # Anyway, what happens when our window invariant is broken? Well, we want to repair the window.. 

        # 2 Questions we have to answer...
        # What data structure makes the most sense to use for our window? likely a hashmap so we can know the most frequent
        # But what does repair mean for our window?

        A = defaultdict(int)
        l, r, maxlength = 0, 0, 0

        while r < len(s):
            # Add r to the window first, otherwise the map could be empty on the first pass and max will have nothing to look at
            A[s[r]] += 1

            # Whatever has the highest count in our map
            desiredChar = max(A, key=lambda c: A[c]) # O(26)

            # Everything that isn't the desired char has to be replaced, so the number of replacements
            # we need is the window length minus how many of the desired char we have
            # Asfar as that is more than k, our window is broken so we keep repairing it from the left
            while sum(A.values()) - A[desiredChar] > k:
                A[s[l]] -= 1
                l += 1

                # We should update our desiredChar btw because a char can change who the most frequent one is
                desiredChar = max(A, key=lambda c: A[c])
            
            # Update the maxlength
            maxlength = max(maxlength, sum(A.values()))
            r += 1

        return maxlength
