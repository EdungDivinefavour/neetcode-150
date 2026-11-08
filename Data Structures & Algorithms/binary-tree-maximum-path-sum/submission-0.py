# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Remember that we want the MAXIMUM path sum
        # So for any given path, we want to be as greedy as possible because if including a path will reduce our sum, we don't want to include it in our calculation

        # One thing to notice is that every path has a topmost node.. ie the one where it branches from
        # So if we ask every node, what is the best path that goes through you? The biggest answer among all of them is our answer

        # We start with root.val and not 0 because a path must have at least one node, and every node could be negative
        maxSum = root.val

        def maxFrom(node):
            nonlocal maxSum
            if not node: return 0

            # First explore everything under me and see what we find
            left = maxFrom(node.left)
            right = maxFrom(node.right)

            # If including my left or right will worsen my sum, don't include it
            if left < 0: left = 0
            if right < 0: right = 0

            # Now let's calculate the maximum path sum that passes through me
            res = node.val + left + right
            maxSum = max(maxSum, res) # Update the maxSum variable with what we computed so far

            # But remember that when returning to my parent, we want to return whichever path was the best
            # We can only hand over one side though.. because if we gave both, the path would split at me and my parent cannot use that
            return node.val + max(left, right)

        maxFrom(root)
        return maxSum