# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Hopefully you are starting to get the hang of recursion
        # For this question, are trying to get the "max" depth. So if one side is longer than one side, we just want to take the longer one.
        # So the question now is... how do we get the height of a given node.
        # Well, when at each node, we can tell that node to count itself, and then add that to the results from its left and right.

        if not root: return 0 # Ofcourse when we get to the end, there is nothing to count

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)