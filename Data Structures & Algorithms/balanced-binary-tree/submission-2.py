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

        def getHeight(node):
            if not node: return 0, True

            leftHeight, leftBalanced = getHeight(node.left)
            rightHeight, rightBalanced = getHeight(node.right)

            height = 1 + max(leftHeight, rightHeight)

            # So basically while getting the height, we just check at once if its balanced or not
            if not leftBalanced or not rightBalanced: 
                return height, False

            isBalanced = abs(leftHeight - rightHeight) <= 1
            return height, isBalanced

        _, isBalanced = getHeight(root)
        return isBalanced