# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # The annoying thing about this question is that n is counted from the end, but a singly linked list
        # only lets us walk forward.. so we cant just count n nodes and stop.

        # There are several ways to solve this problem. Here's one
        # We can flip the whole list first, then the nth from the end becomes the nth from the start! and that we can count

        # I am using a throwaway node in front and its job is basically to hold pre. Don't over think it! The idea is so that for a single node case, we don't have have to handle edge cases separately.
        # That way, pre doesn't have to point to None and the rest of our algorithm works
        pre = dummyNode = ListNode(-1000000, self.reverseList(head))
        curr = dummyNode.next
        
        counter = 1

        while curr:
            # If this is the node we intend to remove, we can point the previous's next to the future node, thereby removing the current node from the list
            if counter == n:
                pre.next = curr.next
                break

            # If not, we are ready to move everything forward for the next iteration
            pre, curr = curr, curr.next
            counter += 1
        
        # Flip it back now that we have removed the desired Node. And now we should go off dummyNode.next and not the head we started with,
        # because if the head was the one we just removed, dummyNode.next is now pointing at the new head
        return self.reverseList(dummyNode.next)
    
    # https://github.com/EdungDivinefavour/neetcode-150/tree/master/Data%20Structures%20%26%20Algorithms/reverse-a-linked-list
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, curr = None, head

        while curr:
            post = curr.next
            curr.next = pre
            pre, curr = curr, post
        
        return pre