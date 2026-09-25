# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # For these abstract data structures, it is a good idea to visualize the problem first by sketching by hand(it forces you to think)
        # If you think about this problem logically, you will realize the following
        # 1. We need a way to hold the Node behind us, because that is what our next has to point to now
        # 2. We need a way to hold the Node in front of us, because the moment we overwrite our next,
        #    the rest of the list is gone and we have no way back to it
        # So as long as we grab the Node ahead before we touch anything, we can safely point our next to the Node behind us

        pre, curr = None, head # pre starts as None because the old head is about to become the tail, and a tail points to nothing

        while curr:
            # At each Node

            post = curr.next # Get a pointer to go ahead of me and hold the next value, before I lose it
            curr.next = pre # Point my next to the previous Node
            
            pre = curr # At this point, I have been reversed so pre can now point to me instead in preparation for next iteration
            curr = post # Then advance me forward
        
        return pre # curr has fallen off the end by now, but pre is sitting on the last Node I reversed, which is the new head