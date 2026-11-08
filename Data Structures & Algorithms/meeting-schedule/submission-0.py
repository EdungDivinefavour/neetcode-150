"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # The first approach coming to my mind is, we can first sort the array by the start times
        # That helps us to guarantee that in a case where there was truly no conflict, the array will be sorted as [(start1, end1), (start2, end2)...]
        # In a case where there is no conflict.. every meeting start must start after the last one's start AND be atleast = or > the last one's end
        # Each end should ofcourse be more than its start

        # After sorting, every start will be arranged from earliest to latest... so we don't really need to check if the current meeting starts before the last meeting(that is already guaranteed)
        intervals.sort(key=lambda interval: interval.start) 

        lastMeeting = Interval(-1, -1)
        for meeting in intervals:

            # If our current meeting starts before the last one ends, then we have a conflict because we can't be in two different meetings
            # We are using < and not <= because (0, 8) and (8, 10) is NOT a conflict.. so if start = last meeting's end, that is still okay
            if meeting.start < lastMeeting.end: return False

            # Update lastMeeting
            lastMeeting = meeting
        
        # If we came this far and we didn't see any conflicts, we can attend all the meetings!
        return True