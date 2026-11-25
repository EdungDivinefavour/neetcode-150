# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # We had earlier worked on a problem "Merge Two Sorted Lists" https://github.com/EdungDivinefavour/neetcode-150/blob/master/Data%20Structures%20%26%20Algorithms/merge-two-sorted-linked-lists/submission-0.py
        # So one way to go about this is to leverage that.. we can start with an empty result and merge lists one by one to that result.. and we will end up with one giant sorted list
        # This works, but if you think about it, our result keeps growing... and every time we merge, we basically walk through all of it again
        # So with say 10,000 lists, the very first elements end up getting walked through about 10,000 times : / We can definitely do better than that

        # We can start with None because merging None with any list will just give us that list back.. so no special condition will be needed for the first list
        res = None
        for i in range(len(lists)):
            res = self.mergeTwoLists(res, lists[i])

        return res

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = curr = ListNode(-10000000)
        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val <= p2.val: curr.next, p1 = ListNode(p1.val), p1.next
            else: curr.next, p2 = ListNode(p2.val), p2.next
            curr = curr.next

        curr.next = p1 or p2
        return merged.next