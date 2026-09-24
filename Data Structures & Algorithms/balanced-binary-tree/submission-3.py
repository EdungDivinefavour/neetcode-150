# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Compared to our earlier brute force solution, If you give this some more thought, you will see that we are doing repetitive work
        # We go all the way down to get the height... and for each height, we then go all the way down again to check if it is balanced ie O(n^2)
        # Remember that the check for balance requires the height of the left and right(and we already get that when traversing for the height)
        # Soo.. we can just use the information we got while we were traversing downward the first time.
        # ie for every node, aside returning its height, we can also return whether its balanced or not

        # There is an even more efficient way to do this without returning a tuple. We can just return -1 whenever a Node is not balanced
        # This way, we save a lot of storage

        def getHeight(node):
            if not node: return 0

            # If left isnt balanced just return -1
            leftHeight = getHeight(node.left)
            if leftHeight < 0: return -1

            # If right isnt balanced just return -1
            rightHeight = getHeight(node.right)
            if rightHeight < 0: return -1

            # If the node itself isnt balanced, return -1
            isBalanced = abs(leftHeight - rightHeight) <= 1
            if not isBalanced: return -1

            # If the node is balanced, return the actual height
            height = 1 + max(leftHeight, rightHeight)
            return height

        return getHeight(root) >= 0



        