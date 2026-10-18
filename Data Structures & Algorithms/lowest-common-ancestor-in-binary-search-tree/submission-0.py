# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # The thing that makes this question easy is that we are in a BST and not some random binary tree
        # Which means that for any Node we are standing on, everything that is smaller than it will be on the left and everything bigger will be on the right
        # So we don't have to go searching around the tree for p and q, we can just compare their values against whoever we are standing on
        # and that will tell us which way both of them would have gone

        # If both of them would have gone the same way, then whoever we are standing on is not their ancestor yet, so we can just keep looking that way
        # But the moment they split up ie one of them goes left and the other one goes right, 
        # then wherever we are standing is the smallest possible parent they can share



        # If both values are bigger than the current Node, we should explore the right
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If both values are smaller than the current Node, we should explore the left
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        



        # If neither of this is the case, because we are in a BST, there cannot be a smaller ancestor at this point between p and q

        
        # This means I am the split point between both nodes and the smallest possible parent they can share
        # If I am not the split point, it doesn't really matter because I am atleast one of them
        return root