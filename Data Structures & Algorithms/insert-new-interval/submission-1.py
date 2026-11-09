class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # The initial intervals list is already sorted and nothing is overlapping... so that's good for us
        # We just need to insert the new interval... To do this, we first have to find the right position.
        # Because the list is sorted, we can just find the rightmost element such that the new start is after its end
        # Anything before that spot ends before the new interval even starts, so we can just copy those over as they are
        out = []
        newStart, newEnd = newInterval

        i = 0
        # New interval normally has to start after the last one ended... the first time that this is not true, we have found the index where we need to insert this interval.
        while i < len(intervals) and intervals[i][1] < newStart:
            out.append(intervals[i])
            i += 1

        # If the intervals are overlapping, ie we are within range of this element or we extend beyond it
        # Since the list is sorted, all we need to ask is.. does this guy start before our end?
        while i < len(intervals) and intervals[i][0] <= newEnd:
            newStart = min(newStart, intervals[i][0]) # Pick the smaller start
            newEnd = max(newEnd, intervals[i][1]) # Pick the larger end
            i += 1 # Keep skipping until we are no longer overlapping

        # Once we are done merging, whatever newStart and newEnd ended up as, is what we go with
        # If nothing overlapped, they are just the new interval itself
        # Whatever is left after i was never touched by the new interval, so we add it back as it is
        return out + [[newStart, newEnd]] + intervals[i:]