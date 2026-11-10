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

        # The last solution works just fine but we were repeatedly doing checks to ensure we weren't out of bounds.. so we can just append a dummy value to the end of intervals
        # And then never use this value.. The idea is that its start is infinity, so it can never overlap with anything
        # That means our inner while loop is guaranteed to stop when it gets to it, so r can never go out of bounds and we don't need the checks anymore : )
        intervals.append([float('inf'), float('inf')])

        r, curr = 0, intervals[0]
        out = []

        # We stop at len(intervals) - 1 because the last element is our dummy value, and it is not a real interval
        while r < len(intervals) - 1:       
            # If the right interval's start is not greater than the current marker's end, they overlap!
            while not (intervals[r][0] > curr[1]):

                # Update current to hold the merged interval so far
                curr = [
                    # Current's start will always be smaller because of our earlier sort so no need to check for min between the two starts.. we can just use curr's.
                    curr[0], 
                    # We however for current's end, we need to use the bigger one between the two
                    max(curr[1], intervals[r][1])
                ]

                r += 1

            # If we get here, the interval at r is not overlapping with curr anymore (or we have hit our dummy value), so we can add curr to out
            out.append(curr)

            # That non overlapping interval is our new curr.. if it is the dummy value, the outer loop ends right after so it doesn't matter
            curr = intervals[r]

        return out