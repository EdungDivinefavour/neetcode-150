# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # This is a somewhat brute force approach btw but the easiest one to reason about
        # Since we know that how to get the height of a tree, we can get the height of the left and right
        # Then at each Node, we can check if the difference between its left's height and right's height is not more than 1
        # Then for us to consider a node balanced, it must itself be balanced but its left and right must also be balanced
        # If we do this down till the leaf nodes, we can just return true since technically(the height of its l and r is not more than 1)


        if not root: return True

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        isBalanced = abs(leftHeight - rightHeight) <= 1

        return isBalanced and self.isBalanced(root.left) and self.isBalanced(root.right)


    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))