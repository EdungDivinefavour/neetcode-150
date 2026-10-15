# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        
        def dfs(node, maxSoFar):
            if not node: return 0

            # A node is considered a good node if it is the biggest from the root to itself. 
            # So we can recursively pass a maxSoFar value if we reach a node and it is bigger than or equal to the max we have seen so far, It is a good node.

            # Process me
            isGoodNode = node.val >= maxSoFar

            # Process left
            left = dfs(
                node.left, 
                node.val if isGoodNode else maxSoFar
            )

            # Process right
            right = dfs(
                node.right, 
                node.val if isGoodNode else maxSoFar
            )

            
            if isGoodNode:
                return 1 + left + right
            else: # If I am a bad Node, no need to count me
                return left + right


        return dfs(root, root.val)
