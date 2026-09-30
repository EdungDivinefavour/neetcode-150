class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We need the nodes grouped by level, so we cant just go down one branch at a time like we normally do
        # We have to finish a whole row before moving to the next one
        # A queue gives us that.. ie first in, first out, so if we only push a node's children,
        # they end up lining up behind everyone already on their own level
        if not root: return []

        queue, result = deque([root]), []
        
        # We want to keep doing this till there is nothing in the queue so that we don't end up abandoning any nodes in there
        while queue:
            level = []

            # This for loop seems straightforward but it is easy to mess up if you don't lock in the length before the iteration,... and you instead use for xxxxx in queue.
            # The reason is that we are mutating this queue as we go, so we have to lock in how many nodes are on this level before we start adding the next level's nodes to it
            # With a deque you at least get a RuntimeError telling you the deque was mutated during iteration.. with a plain list you'll likely get no error at all,
            # and it will just quietly keeps going into the nodes you appended and your levels will come out merged together
            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)

                # Line up my kids for the next round, they will stand behind everyone on my level
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)

            # Add all we found for that level to our result array
            result.append(level)
        
        return result