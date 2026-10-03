# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # The annoying thing about this question is that n is counted from the end, but a singly linked list
        # only lets us walk forward.. so we cant just count n nodes and stop.

        # Here's another approach and we don't need to do the previous O(3n) ie reverse, remove node, reverse again

        # We can first get the length of the list
        length = 0
        curr = head

        while curr:
            length += 1 # Count this node
            curr = curr.next # Move forward for the next iteration
            
        # Now that we have the length of the list, if we subtract n from the length, we get the position of the node we intend to delete
        # ie if we have 10 elements.. and we want to remove the 3rd from the back, 10 - 3 = 7
        # So this is the 7th Node from the front
        # I deliberately lied.. that last statement is not true... Try to draw it out.
        # The 3rd element from the back is the 8th Node! not the 7th one. Let's count Node10, Node9 anddddd Node 8. thats who we want to remove
        # This is the case because we have to "also" count the last Node
        # We should do 10 - 3 + 1


        # I'm using a dummyNode to start things off just so I don't handle any special edge cases for a single node
        dummyNode = pre = ListNode(-100000000, head)
        curr = dummyNode.next

        counter = 1
        while curr:
            if counter == length - n + 1:
                pre.next = curr.next
                break
            
            counter += 1
            pre, curr = curr, curr.next
        
        return dummyNode.next
