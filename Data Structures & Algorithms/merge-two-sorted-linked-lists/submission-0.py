# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # For this problem, If had been guaranteed that the lists were sorted such that every element in one is smaller than every element in the other eg 1234, 5678..
        # We would have simply appended the bigger list to the smaller one
        # But because we can have some elements that are bigger than some between the two lists eg 124, 135, we need a way to carefully pick the elements one after the other
        # There are different ways to solve this problem(although they will likely lean on the same idea of 2 pointers)
        # Iteratively this feels like it will be a headache but lets give it a try

        # Starting with a throwaway node saves us from doing a special case for the very first pick.
        # Without it we would have to ask "is this the first element?" on every single iteration just to know
        # whether to set the head or to append, so we let merged hold the junk Node and return whatever comes after it
        merged = curr = ListNode(-10000000)
        p1, p2 = list1, list2

        while curr:
            # The moment one list is finished, the other one is sorted and every element in it is bigger
            # than everything we have already placed, so there is nothing left to compare.
            # We can hang the whole rest of it off the end in one shot and stop
            if not p1: 
                curr.next = p2
                break
            elif not p2: 
                curr.next = p1
                break

            # Both lists still have something, so take the smaller of the two and only advance that list.
            # We are using <= rather than < so that equal values keep the order they came in
            if p1.val <= p2.val:
                curr.next = ListNode(p1.val)
                p1 = p1.next
            else:
                curr.next = ListNode(p2.val)
                p2 = p2.next
            
            curr = curr.next # Move to the node I just placed, since that is the new end of the merged list
            
        return merged.next # Skip the throwaway node and return the real head