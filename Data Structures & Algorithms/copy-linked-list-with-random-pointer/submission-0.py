"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # The tricky part of this question is the random pointer. It can point to any node in the list, including one that is way ahead of us that we haven't copied yet.. 
        # So if we try to build the copy in a single pass, we will run into a random pointer that has nothing to point to yet
        # One way I can think to go around this is to do it in two passes. In the first pass we create every copy, and in the second pass we connect them
        # That way, by the time we start wiring pointers, every copy already will exist and nothing will be missing and ach old node will point to its brand new copy. 
        
        # We are also adding None pointing to None upfront, because next and random can both be null
        # This way we don't have to write a special case for them when we are connecting things
        copies = {None: None}

        # First, we make a copy of every node. Note that these copies have no next or random yet, we will add those in the next pass
        cur = head
        while cur:
            copies[cur] = Node(cur.val)
            cur = cur.next

        # Second, Now that every copy exists, we can walk the old list again and wire up each copy
        cur = head
        while cur:
            copy = copies[cur]

            # My copy's next should be the copy of my next, and same for random.
            # We don't really care how far away they are, the map will give us their copies immediately
            copy.next = copies[cur.next]
            copy.random = copies[cur.random]

            cur = cur.next

        # The copy of the head we were given is the entry point to the whole new list
        return copies[head]