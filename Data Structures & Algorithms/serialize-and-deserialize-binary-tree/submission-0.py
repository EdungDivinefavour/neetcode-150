# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # For this question, we can use pre order traversal to serialize the tree into a string
        # This is because preorder gives us the root first, so it will make it easier for us to deserialize later.
        # So we can store string = root1#left1#right1#root2#left2#right2 etc etc

        # We can either build our string directly like so
        # serialized = ""
        # def dfs(node):
        #     nonlocal serialized
        #     if not node: 
        #         serialized += "#N"
        #         return

        #     serialized += "#" + str(node.val)
        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(root)
        # return serialized

        # Or for the sake of saving on some compute, we can add everything to an array and build the string once at the end
        arr = []
        def dfs(node):
            if not node:
                arr.append("N")
                return

            arr.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return "#".join(arr)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # First we want to convert the string into an array to make our lives easier when we need to index.
        arr = data.split("#")

        # Remember that because we built the array in preorder, any root we encounter will come first, before all it's lefts.. and finally all it's rights
        # So we can just move an index variable through our array and say.. Hey, construct my root... and pass this call over to my left and right
        # The reason why we have to increase this index variable is because in the absence of that, after say the left is done contructing, we don't want the right to go contructing from the same index
        # We need it to know which elements we are done with so it will only look at elements after that index
        index = 0
        def dfs():
            nonlocal index
            if arr[index] == "N": 
                index += 1
                return None

            root = arr[index] # The element at my current index is my root
            index += 1 # Increase the index so that the next recursive call knows what index it should be looking at

            # Contruct this Node, the recursively construct the left and right
            return TreeNode(int(root),  dfs(), dfs())
        
        return dfs()
