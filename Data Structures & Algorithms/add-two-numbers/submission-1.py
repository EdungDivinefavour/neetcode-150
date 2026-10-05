# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # We already did the iterative one, so now lets have some fun with recursion!
        # The reason recursion works so well here is that once we have added one column and worked out its carry,
        # whatever is left is just two smaller lists and a carry.. which is the exact same problem all over again
        # So instead of tracking pointers by hand, each call just answers "what digit am I" and then asks the next guy for the rest

        # The carry has to move along as a parameter, because the next column cant do anything without it
        def add(l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0):
            # This is our base case ie both lists are finished
            # But we cant just return None here, because that leftover carry might still need a Node of its own ie 5 + 5
            # So if there is a carry hanging around, it becomes the very last digit
            if not l1 and not l2:
                return None if not carry else ListNode(carry)
            
            # One list can run out before the other, so we only add in whoever is still around
            if not l1: 
                total = l2.val + carry
            elif not l2:
                total = l1.val + carry
            else:
                total = l1.val + l2.val + carry
            
            # Only the ones digit of our total will stay behind in this Node, anything above that gets passed along as the carry
            # And by the time the recursive call comes back, it would have already been built by the entire rest of the answer for us to point at
            return ListNode(
                total % 10,
                add(
                    l1.next if l1 else None, 
                    l2.next if l2 else None,
                    1 if total >= 10 else 0 # Each column can only ever carry 1, since even 9 + 9 + 1 is still just 19
                ),
            )

        return add(l1, l2)