class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # So we are trying to find the shortest substring where t exists(including its duplicates).
        # The first thought that comes to my mind is sliding window!
        # What truth do we want to maintain in our window? If you think about the question, we want to maintain the fact that A always reflects what our window contains relative to t
        
        # Keep moving r to the right and reducing from our window(if we find anything in our window) as we go right
        # Keep doing that until we have exhausted everything in our window from the right so far.
        # We can store that window..
        # Then after the exhaustion from the right, our window is valid, so we can shrink from the left since there may be characters we don't need
        # While shrinking from the left... if window is exhaused, store the updated string... 
        # If window ends up having any positive count, stop shrinking from the left... we now have room to expand from the right
        # Ofcourse while shrinking from the left, if we meet someone in our window, we should restore it in the window

        A = {}
        for c in t: A[c] = 1 + A.get(c, 0)

        # In our last solution, we rebuilt the string from scratch everytime inside the while loop
        # This is because of a limitation in python as strings are not mutable. 
        # The cost of doing that was that our solution did not work for very very long string
        # So instead of rebuilding the string everytime, we can just store a tuple with our smallest l,r pair.. and then just build the result string once at the end
        res = (0, float('inf'))
        l, r = 0, 0
        while r < len(s):
            # While moving r, if we meet a member of our window, lets deduct it from count
            if s[r] in A: A[s[r]] -= 1

            # If we have deducted everything in our window ie we have a valid substring(may not be our min), but we have a valid one, we can try shinking from the left to see how small we can get
            # Our counts can sometimes go negative if our window has extra duplicates, that is why we check <= 0 and not == 0 eg s = "aab", t = "ab"
            while all(value <= 0 for value in A.values()):
                # Its possible we have not yet stored anything in the res pair yet
                
                # Store the updated string if its smaller
                start, end = res
                if r - l < end - start: res = (l, r)

                # While shrinking from the left, if we meet something in our window, we should restore its count
                if s[l] in A: A[s[l]] += 1
                
                # Then advance l
                l += 1

            # Our window is no longer valid, advance r forward.. we are ready to expand
            r += 1

        start, end = res
        return (
            "" if end == float('inf') else # If we haven't updated min since we started, return ""
            s[start: end+1]
        )