# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # We can do better than our last solution. 
        # Remember that when we want to get the diameter, we traverse all the way down to get the height, and then traverse all the way down again to ask the diameter question for every subtree ie O(n^2)
        # Do you spot any redundancies? We walk past the same node repeatedly to get the same information.. what if we just returned that information when we walked down the first time?
        # So instead of returning one number, we can make every call to hand us back both answers at once

        def dfs(node):
            if not node: return 0, 0

            leftDiameter, leftHeight = dfs(node.left)
            rightDiameter, rightHeight = dfs(node.right)

            diameter = leftHeight + rightHeight # This gives my diameter
            height = 1 + max(leftHeight, rightHeight) # This gives my height

            # The widest path might not pass through me at all, it could be inside one of my subtrees.
            # But they already worked that out and handed it up, so I just take whichever of the three is biggest
            return ( # And then return both the biggest diameter so far as well as the height
                max(diameter, leftDiameter, rightDiameter),
                height
            )
            
        return dfs(root)[0]