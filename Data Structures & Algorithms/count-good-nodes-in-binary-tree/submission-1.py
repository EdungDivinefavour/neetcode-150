# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSoFar):
            if not node: return 0

            # A node is considered a good node if it is the biggest from the root to itself. 
            # So we can recursively pass a maxSoFar value if we reach a node and it is bigger than or equal to the max we have seen so far, It is a good node.

            # I think we can further clean up our last solution

            # Process left
            left = dfs(node.left, max(maxSoFar, node.val))

            # Process right
            right = dfs(node.right, max(maxSoFar, node.val))

            return (
                (1 if node.val >= maxSoFar else 0) + left + right
            )

        return dfs(root, root.val)
