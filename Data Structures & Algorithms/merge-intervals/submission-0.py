class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # To preserve some sort of order to help us solve this problem, we would have to sort the array first
        # After doing that, we can keep a running interval ie curr at the start... and start moving a right pointer r
        # If the interval at the right pointer has a start that is not greater than curr's end, it is overlapping.
        # Update curr such that its start should be the smaller of the two... and its end should be the bigger of the two.
        # Then move the right pointer forward
        # If the new interval we encounter is not overlapping, then we can add the curr to the output array and make that first interval outside the overlap our new curr.
        
        # Because we sorted by start, any interval that can overlap with curr will always be the next one(s) in the array
        intervals.sort(key=lambda x: x[0])

        r, curr = 0, intervals[0]
        out = []

        while r < len(intervals):       
            # If the right interval's start is not greater than the current marker's end, they overlap!
            while r < len(intervals) and not (intervals[r][0] > curr[1]):

                # Update current to hold the merged interval so far
                curr = [
                    # Current's start will always be smaller because of our earlier sort so no need to check for min between the two starts.. we can just use curr's.
                    curr[0], 
                    # We however for current's end, we need to use the bigger one between the two
                    max(curr[1], intervals[r][1])
                ]

                r += 1

            # If we get here, the interval at r is not overlapping with curr anymore (or we have run out of intervals), so we can add curr to out
            out.append(curr)

            # That non overlapping interval is our new curr.. as long as we haven't gone through everything
            if r < len(intervals): curr = intervals[r]

        return out