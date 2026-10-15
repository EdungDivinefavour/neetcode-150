# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # The key to this question is remembering the fact that a BST has the smaller elements always to the left

        # We can simply traverse through in inorder because it goes left first, center next, and then right last.
        # We don't even need an array because each new node will be bigger than the last. So we can just store the kth value when we find it

        count, kth = 1, None
        def dfs(node):
            nonlocal kth, count
            if not node or kth is not None: return

            dfs(node.left)
            if count == k: 
                kth = node.val
            count += 1
            dfs(node.right)
        
        dfs(root)
        return kth