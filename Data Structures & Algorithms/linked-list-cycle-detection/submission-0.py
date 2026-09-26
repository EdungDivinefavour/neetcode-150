# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # This question is a bit tricky if you've never heard of the tortoise and hare algorithm
        # The idea is that we start with two pointers 'slow' and 'fast'. 
        # One pointer will move twice as fast as the other and if they ever meet, we have a cycle
        # This is because at some point in a cycle, the fast pointer will move so far ahead that it will come around and meet the slow one
        # Imagine two runners running in a cycle.. if one is running at some pace and the other is running twice as fast, the fast runner will eventually catch up with the slow runner
        # But if there were no cycle, the fast runner will just forever outpace the slow runner.

        slow = fast = head
        
        # We never expect fast and fast.next to ever be null in a cycle because the list will never end
        # So falling out of this loop is itself our proof that we reached an end, meaning there is no cycle.
        # We also check fast.next and not just fast because fast takes two steps at a time,
        # and without that we would blow up trying to read next on a null

        while fast and fast.next:
            # Move first, then compare. If we compared at the top they would match instantly on the first pass, since they both start on head
            slow = slow.next
            fast = fast.next.next

            if slow == fast: return True

        return False