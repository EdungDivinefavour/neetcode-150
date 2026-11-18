# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # There are a few thoughts that come to mind here.. One of which is just going the lazy route and merging the lists using the language's sorting function
        # Then when we just go through the list elements and build our linkedList from there : )
        # It kinda works, but we are not really making use of the fact that every list we were given is already sorted.. so we will come back to that in the next solution

        # First we go through every list and dump all the values into one big array
        merged = []
        for linked in lists:
            curr = linked
            while curr:
                merged.append(curr.val)
                curr = curr.next
        
        # Then we can sort the merged list
        merged.sort()

        # Then create a dummy Node just so we don't have to create any special conditions in the for loop
        # The value we give it doesn't matter because we never return it.. we return whatever comes after it
        curr = head = ListNode(-100000000)
        for num in merged:
            curr.next = ListNode(num)
            curr = curr.next
        
        return head.next