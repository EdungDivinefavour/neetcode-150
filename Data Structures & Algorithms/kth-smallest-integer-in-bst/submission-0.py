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
        # And then store everything in an array, we can just return the k-1th element ie if we have [1,2,3,4,5,6,7,8] and we want the 3rd element, we will just return array[3-1]

        store = []
        def dfs(node):
            if not node: return

            dfs(node.left)
            store.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return store[k-1]