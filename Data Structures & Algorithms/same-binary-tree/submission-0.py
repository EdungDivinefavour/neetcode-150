# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # As usual, recursion is the most intuitive way to traverse trees(trust me)
        # To check if a tree is same as another tree, we can break this problem into its smallest part which is basically testing each Node.
        # So we can check if at each Node, our p Node is same as its q sibling
        # To consider any 2 nodes to be 'same', their value has to be same... But also, their left and right has to be the same.

        # If they get to a point where both Nodes are null, we can consider them equal
        if not p and not q: return True 

        # If they are not "both" null, and one of them somehow one of them is Null, they are definitely not equal
        if not p or not q: return False
        
        isLeftSame = self.isSameTree(p.left, q.left) # Traverse left
        isRightSame = self.isSameTree(p.right, q.right) # Traverse right

        return p.val == q.val and isLeftSame and isRightSame