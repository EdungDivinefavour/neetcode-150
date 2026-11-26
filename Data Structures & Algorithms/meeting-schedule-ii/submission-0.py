"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # So first off, we want to deal with the meetings in the order in which they start
        # Because it wouldnt really make sense to book a meeting for a later time and then
        # use that to determine if a room is available for an earlier meeting
        intervals.sort(key=lambda x: x.start)

        # Now initially I was thinking of using a stack to keep track of the rooms
        # The problem with that is that the last meeting we added to the stack isnt necessarily the meeting that will end first..
        # and there might be some other room in the stack that is already available

        # We could go through every single room and check if any one of them is available but then again.. if the meeting with the earliest ending time hasnt ended,
        # then surely none of the other meetings would have ended either

        # So to rephrase our thinking,
        # Imagine a real office.. if we wanted to book a meeting and a couple of rooms are already occupied, naturally we would want to know which of those rooms will be available first

        # So we essentially just want to keep track of which room has the earliest ending time at any given point
        # Hence the minheap
        heap = []

        for interval in intervals:
            # If we have an existing room and its meeting ends before or at the time our meeting starts
            # then we can essentially replace that meeting with ours and reuse the room
            if heap and interval.start >= heap[0]:
                heapq.heappop(heap)

            # Regardless of whether we found an available room or not, our meeting has to happen
            # So we are either updating the ending time of an existing room or creating a new room entirely
            heapq.heappush(heap, interval.end)

        # Initially I was keeping track of the max length the heap ever had
        # But notice that we never actually get rid of a room.. we either reuse one or create a new one
        # So the size of the heap will never decrease between iterations
        # Hence the length of the heap at the end is basically how many rooms we ever needed
        return len(heap)