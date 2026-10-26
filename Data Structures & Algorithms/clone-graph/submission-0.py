"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # The tricky thing about this question is that a graph can have cycles, so if we just clone a node and then clone
        # its neighbors, and their neighbors... we would eventually come back to a guy we already cloned and keep going forever
        # So we need a way to remember who we have already cloned.. and a hashmap is perfect for that!
        # Each old node will point to its brand new copy. This way, whenever we meet an old node again, we don't create
        # a second copy of it, we just usethe one we already made

        if not node: return None # We have nothing to clone, so there is nothing to return

        # We can start by cloning the very first node. Note that the clone has no neighbors yet, we will hook them up as we go
        clones = {}
        clones[node] = Node(node.val)

        # We are doing a BFS here(DFS works too, there is a recursive version) so we need a queue to hold the old nodes whose neighbors we are yet to look at
        q = deque([node])

        while q:
            cur = q.popleft()

            for neighbor in cur.neighbors:
                # If we have never met this neighbor before, it doesn't have a clone yet, so we make one for him
                # And we only add him to the queue here, because this is the first time we have seen him.
                # If we added him every time we met him, we would loop around in a cycle forever
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                # Whether the neighbor was brand new or not, his clone exists by now. So we can connect my clone to his clone
                # Notice this is outside the if on purpose.. we still need to draw the connection even for neighbors we have already cloned
                clones[cur].neighbors.append(clones[neighbor])

        # The clone of the node we were given is the entry point to the whole new graph
        return clones[node]