class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # The initial intervals list is already sorted and nothing is overlapping... so that's good for us
        # We just need to insert the new interval... To do this, we first have to find the right position.
        # Because the list is sorted, we can just find the rightmost element such that the new start is after its end
        # Anything before that spot ends before the new interval even starts, so we can just copy those over as they are
        out = []
        newStart, newEnd = newInterval

        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            
            # The new interval normally has to start after the last one ended... 
            # The first time that this is not true, I have found the index where I need to insert this interval.
            if not newStart > end:

                # If the intervals are overlapping, ie I am within range of this element or I extend beyond it
                # Since the list is sorted, all we need to ask is.. does this guy start before my end?
                while i < len(intervals) and start <= newEnd:
                    newStart = min(newStart, start) # Pick the smaller start
                    newEnd = max(newEnd, end) # Pick the larger end

                    i += 1 # Keep skipping until we are no longer overlapping
                    if i < len(intervals): start, end = intervals[i] # Update start and end for next iteration

                # Once we are done merging, whatever newStart and newEnd ended up as, is what we will go with
                # If nothing overlapped, they are just the new interval itself
                else:
                    start, end = newStart, newEnd

                out.append([start, end])
                break
                
            # If we haven't found the insertion index yet, move i forward
            # This guy ends before the new interval starts, so he goes into out exactly how he was
            else: i += 1
            out.append([start, end])

        # If we got through the whole list without ever finding the spot, then everyone ended before the new interval started
        # Which means the new interval should just go to the very end
        else:
            out.append(newInterval)

        # Whatever is left after i, was never touched by the new interval, so we can add it back as it is
        return out + intervals[i:]