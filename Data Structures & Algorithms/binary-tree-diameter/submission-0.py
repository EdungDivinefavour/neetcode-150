# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # A brute force approach to this problem will be to traverse down the tree to get the heights of the left and right
        # And after getting the heights, we can sum them to get the diameter from that Node(imagine standing on a Node and spreading your hands)
        # Now when you have that Node's diameter, we want to compare it with the diameters of the other nodes in the tree(which we ofcourse get by traversing left and right)
        # Whichever of those is biggest is the answer

        def getHeight(node):
            if not node: return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))

        if not root: return 0
        myDiameter = getHeight(root.left) + getHeight(root.right) # the widest path that actually passes through me

        # But the widest path in the whole tree might not go through me at all, it could be buried
        # entirely inside one of my subtrees, so I have to ask them the same question too
        return max(
            myDiameter,
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right)
        )