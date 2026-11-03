# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        # So our previous solution works but is wasteful at two things
        # 1. inorder.index() scans through the array every single time we need to find the root, that is O(n) work everytime
        # 2. Also slicing in python creates a brand new copy of the list every time, so we keep copying chunks of preorder and inorder on every call

        # So one way around this is that, we can build a hashmap of value to index in inorder once, so finding the root becomes O(1)
        # For 2, instead of breaking up the list, we can just leave them alone and instead keep track of which part of inorder we are looking at using l and r

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # So basically same idea as before, preorder tells us the root and inorder tells us what is on its left and right
        # We just don't want to rediscover where everyone is in inorder every time, so we do it once upfront
        indices = {val: idx for idx, val in enumerate(inorder)}

        # Since we are no longer slicing preorder, we need something to tell us who the next root is
        # Preorder is root, left, right.... sooo as we build the tree, we just need to walk through preorder one element at a time
        # Every time we create a node, we can move this pointer forward
        self.pre_idx = 0

        # l and r are the boundaries of inorder that we are currently building a tree from
        def dfs(l, r):
            # If l has crossed r, then there are no nodes left in this section of inorder, so there is no tree here
            # This basically replaces our old check of the lists being empty
            if l > r: return None

            # The next element in preorder is the root of the tree we are building right now
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Find where the root is located in inorder, so everything between l and mid-1 is the left subtree, and everything between mid+1 and r is the right subtree
            mid = indices[root_val]

            # The order is especially important, ie we have to build the left subtree first
            # Preorder is root, left, right.. so this means the next elements in preorder belong to the left subtree, and only after it is done can we reach the right subtree's elements
            # Because our pointer only moves forward, building left first makes sure it lands on the right nodes at the right time
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            
            return root

        # At the start, we are looking at the whole of inorder
        return dfs(0, len(inorder) - 1)