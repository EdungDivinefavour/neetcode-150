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
        # Now lets have some fun with recursion!

        # The reason recursion works really well here is that once you pick the smaller front element,
        # what is left over is just two smaller sorted lists, which is the exact same problem again.
        # So instead of tracking pointers by hand, we let each call answer "what comes after me?"

        # If one of them is empty, return the other
        # This is also our base case, because every call shortens one of the lists by a node,
        # so we are guaranteed to hit an empty one eventually and stop
        if not list1: return list2 
        if not list2: return list1

        # Take whichever head is smaller, and let the recursive call figure out the rest of the merge.
        # By the time it returns, it will already hand us a finished sorted list to point our new node at
        if list1.val <= list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
