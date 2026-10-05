# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # The first thing that looks weird about this question is that the digits are stored backwards.
        # But you see, thats actually doing us a favour! The ones digit comes first, so we can just add left to right
        # exactly the same way we would do it on paper
        # There are a couple of ways to solve this. Here's the iterative one, there is a recursive version too

        p1, p2 = l1, l2

        # Another throwaway node so we dont have to treat the very first digit we create as a special case
        dummyNode = curr = ListNode(-10000000)
        carry = 0

        # We keep going for as long as either list still has digits... and also while there is a carry value,
        # because that carry might still need a whole new digit of its own even after both lists have finished ie 5 + 5
        while p1 or p2 or carry:

            # One list can run out before the other, so we only add in whoever is still around
            if not p1 and not p2:
                total = carry
            elif not p1: 
                total = p2.val + carry
            elif not p2:
                total = p1.val + carry
            else:
                total = p1.val + p2.val + carry
            
            # Only the ones digit of our total will stay behind in this Node, anything above that has to be carried over
            curr.next = ListNode(total % 10)

            # We only step forward on a list that still has something left, the finished one just remains at None... If not we'll get a null pointer exception
            if p1: p1 = p1.next
            if p2: p2 = p2.next
            
            curr = curr.next

            # Each column can only ever carry 1, since even 9 + 9 + 1 is still just 19
            carry = 1 if total >= 10 else 0

        return dummyNode.next # Ofcourse throwaway the throwaway node, and return its next 