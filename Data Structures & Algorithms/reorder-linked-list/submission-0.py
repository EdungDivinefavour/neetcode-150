# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # One way I can think to approach this problem is to reverse the second half of the list and then merge the left and right half
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        # The right half would basically be everything after the middle
        # So I am always going to have either equal to or less elements on my right than on my left
        right = mid.next
        # We can cut off right half from the head so that we know we only have the left half
        mid.next = None

        # Now we have the left and the reversed the right and we can start merging both lists
        left, right = head, self.reverse(right)

        while right:
            post = left.next # Hold the node in front

            temp = right # Hold the new guy from right that we want to use
            right = right.next # Move our right pointer one Node forward
            temp.next = None # Clear the next for the Node that we want to append to left
            
            left.next = temp # Add that new guy to left
            temp.next = post # Add the remaining part of left to the new guy

            left = post # Advance left forward

        
    # I won't go into explaining this but here's the logic behind the reversal if you are not already familiar with it
    # https://github.com/EdungDivinefavour/neetcode-150/tree/master/Data%20Structures%20%26%20Algorithms/reverse-a-linked-list
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, curr = None, head
        while curr:
            post = curr.next
            curr.next = pre

            pre, curr = curr, post
        
        return pre