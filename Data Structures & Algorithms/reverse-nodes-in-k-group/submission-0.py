
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # So my first thought is that we already know how to reverse a linked list.. 
        # Why don't we just reverse k nodes at a time?..... But we have to be careful about two things here
        # 1. We should only reverse a group if it has exactly k nodes, otherwise we should leave those nodes as they are.. per the question
        # 2. Once we reverse a group, how do we connect it to the group we reversed before it?
        
        # We can easily tell how many complete groups we have by doing the following
        LEN = self.getLength(head)
        GROUPS = LEN // k

        # If we don't have one complete group, then return the head... Nothing to really do here
        if GROUPS == 0: return head

        # So we keep two pointers.. when we intend to rotate... begin to remember where our current group started.. and curr which will move k times to reach the end of our desired rotation Node
        begin, curr = head, head
        res = None

        # We need to remember the tail of the previous reversed group so that we can connect it to the head of the next reversed group
        previousTail = None

        # This is how many groups we want to try the reversal for
        for i in range(GROUPS):

            pre = None # We are starting a completely new reversal.. so pre should be None

            # Reverse the nodes k times
            # There are already too many things to keep track of here.. so why use a while loop with another count variable when we already know we want exactly k reversals?
            for _ in range(k):
                post = curr.next
                curr.next = pre
                pre, curr = curr, post

            # So after reversing k nodes, pre is now the new head of this group, begin is the new tail and curr is pointing at the next group
            # ie if we reversed the first two nodes of 1, 2, 3, 4, 5 then pre would be at 2, begin at 1 and curr at 3

            # We should store the very first reversal as that will be our new head
            if i == 0: res = pre

            # Now how do we connect this reversed group to the previous one?
            # Well, we know pre is the new head of this group.. so if we remembered the tail of the previous group, we can just connect it to pre
            # ie when we reverse 3 and 4, pre would be at 4 and previousTail would be at 1.. so we can connect 1 to 4
            if previousTail: previousTail.next = pre

            # At this point, curr would be pointing at the node just after our last reversal ie the new start position
            # And since begin is now the tail of the group we just reversed, we can connect it to curr
            begin.next = curr

            # But begin is also the new tail of the group we just reversed
            # So lets save it.. because we will need to connect it to the next reversed group
            previousTail = begin

            # Then set begin and curr to our new start positin so that we can start our next reversals
            begin = curr

        return res

    def getLength(self, head) -> int:
        if not head: return 0

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        return length
