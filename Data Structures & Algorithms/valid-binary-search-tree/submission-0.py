# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # At first glance you might want to perform just 2 checks ie
        # My left has to be smaller than me and my right has to be bigger than me.. like so
        # isValid = (
        #     root.left.val < root.val and
        #     root.right.val > root.val
        # )
        # But imagine a tree that looks like this
        #  10
        # /  \
        # 5    15
        #     /  \
        #    6    20
        # Our check will wrongly pass this tree because while Node 15 in itself meets the requirement, the entire tree does not meet the requirement
        # Think about constraint 1 and 2 carefully... it says the 'left subtree' must contain smaller Nodes... It didn't say the left Node alone should be smaller.. It says the entire left subtree
        # Same with the right subtree and that is why our check above will not work
        
        # A good way to think about this problem instead is in terms of boundaries i.e.
        # For each node, what is the range of values it is allowed to have?
        # A left child should be anywhere from its parent's lower bound to it's parent's value..
        # A right child should be anywhere from its parent to the parent's upper bound..

        def dfs(node, lower, upper):
            if not node: return True
            
            isValid = lower < node.val < upper
            return (
                isValid and
                dfs(node.left, lower, node.val) and
                dfs(node.right, node.val, upper)
            )
        
        # At the root there are no limits yet, so that is why we start with -inf and +inf
        return dfs(root, float('-inf'), float('inf'))