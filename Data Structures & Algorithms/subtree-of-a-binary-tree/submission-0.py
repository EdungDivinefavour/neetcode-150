# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # To determine if a tree is a subtree of another tree
        # It has to be same with either the left or the right of the other tree
        # The question also says a tree can be a subtree of itself
        
        def isSameTree(p, q):
            # Hopefully you have solved the question of same tree before this, if not see
            # https://github.com/EdungDivinefavour/neetcode-150/tree/master/Data%20Structures%20%26%20Algorithms/same-binary-tree
            if not p and not q: return True
            if not p or not q: return False

            return (
                p.val == q.val and 
                isSameTree(p.left, q.left) and
                isSameTree(p.right, q.right)
            )

        # We ran out of tree, so there is nowhere left for subRoot to be. This is also what makes our root.left/root.right check below safe
        if not root or not subRoot: return False

        # So we can simply recursively check if subRoot is same as root or if its same as root's left or root's right.
        # If any of that is true, then subRoot is a subtree of root
        # Note the calls are different on purpose: isSameTree compares, isSubtree searches
        
        # At every node we should ask two different things.
        # First, is the whole tree starting from here identical to subRoot(isSameTree)?
        # If not, then subRoot might still be buried somewhere further down, so is it somewhere inside this tree?
        # So it is the exact same question we started with, but just on a smaller tree.. ie we hand it back to isSubtree
        # This is why the two calls are different: isSameTree compares, isSubtree searches
        return (
            isSameTree(root, subRoot) or
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )