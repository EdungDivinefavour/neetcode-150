# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # At the core of this problem is a breadth first search algorithm because we want to display whatever Node is at the higher levels first before the lower levels
        # Because we want to print the rightmost Node, we will ultimately be printing only one Node per level
        # Which is basically the rightmost one we see first. After which we can go on to the next level

        # To do level order processing, we need a queue
        # Starting it empty when root is None, so that the loop below will just never run and we return an empty array
        res = []
        queue = deque([root]) if root else deque()
        
        while queue:
            # At every start of this loop, we are about to process whatever is in our queue which is basically all the elements in that level
            # And since we always add left before right, the queue is holding this level in left to right order
            # So the last Node in the queue is our rightmost one... we can just peek at him, we don't want pop him because he still has children to give us
            res.append(queue[-1].val)

            # For all our queue members, we want to add their children to the queue
            # Same as the level order question we solved earlier.. we want to lock in len(queue) first, because we are about to add the next level to this same queue
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            
        return res