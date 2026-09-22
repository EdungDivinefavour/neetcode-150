# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # The most intuitive way to traverse trees is usually with recursion
        # If we think about how we can achieve this with recursion (which hopefully you already have an idea of)
        # We can break this problem down into its smallest parts which is basically to invert each individual Node
        # If we do that we will end up with a full inverted tree
        # So with recursion, we can simply invert the root node and set the left to be the inverted right.. vise versa for the left

        
        if not root: return None # If we hit the end of our tree, dont bother doing anything

        return TreeNode(
            root.val,
            self.invertTree(root.right),
            self.invertTree(root.left)
        )
        