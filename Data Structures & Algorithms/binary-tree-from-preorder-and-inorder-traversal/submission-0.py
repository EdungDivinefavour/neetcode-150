# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # The first thing we want to figure out is what each traversal actually tells us
        # Recall that preorder goes root, left, right.. so the first element is always the root of the tree we are looking at
        # Inorder goes left, root, right.. so if we know who the root is, everything to its left in inorder is the left subtree and everything to its right is the right subtree
        # That means if we can find the root, we can split the problem into a left tree and a right tree, and then solve each of those the same way

        # If we have no nodes left to place, so there is no tree to build
        if not preorder or not inorder: return None

        # Preorder tells what is the root
        root = TreeNode(preorder[0])

        # Now that we found the root in inorder, everything before it is the left subtree and everything after it is the right subtree
        # mid is also the number of nodes in the left subtree, which we will need for preorder
        mid = inorder.index(preorder[0])

        # For the left subtree, inorder is straightforward, it is basically everything before mid
        # For preorder, we need to skip the root at index 0, and the next mid elements are the left subtree.. hence we go up to mid + 1
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

        # For the right subtree, inorder is everything after mid
        # For preorder, whatever is left after the root and the left subtree has to be the right subtree
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root