class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # I want to create some sort of 'fixed' window from s1 that contains the characters in s2
        # Then from that window, I want to overlay it ontop of s2 from the beginning and then start moving right
        # For each slide to the right, I want to ask... have I consumed all the counts in my window?.. If yes I return True
        # Remember the idea behind a sliding window is that, we have to maintain a truth the whole time inside the window
        # The truth we are trying to maintain here is that our window contains an accurate count of every char in between l and r(that is from s1)

        # First thing we want to figure out is how we create our window?. 
        # The best way to keep count of the character occurences will be a hashmap!
        A = {}
        for c in s1: A[c] = 1 + A.get(c, 0)
        
        # Now I know the occurence of every character in s1 ie I have my window

        l, r = 0, 0
        while r < len(s2):
            # If we encounter a right that is in the window, subtract from it
            if s2[r] in A: A[s2[r]] -= 1
            
            # If we haven't covered as many chars as s1, we don't have enough grounds to start overlaying our window
            if r < len(s1)-1: 
                r += 1
                continue
            
            # At this point, we are ready to overlay our window ontop of s2 and ask our questions
            # If all the characters are currently at 0, this is a valid map
            if all(count == 0 for count in A.values()): return True

            # Slide window forward and ofcourse revert whatever decision we had made to the window due to l
            if s2[l] in A: A[s2[l]] += 1
            l += 1
            r += 1

        return False
