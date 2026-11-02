class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # This question asks us to check whether a graph is a valid tree... At first though you might immediately imagine a binary tree buuuuut thats not what the question asked : )
        # It says to check if the graph is a tree! Remember a Trie prefix has a tree like structure, a linkedlist-like structure mathematically speaking also is a tree in that sense.
        # So with this loose definition of a tree, what makes a graph a valid tree?

        # Well, think about a regular tree that comes to your mind.. One thing is for sure, it has no cycles.. so that's atleast one of the conditions
        # But the absence of cycles does not necessarily make the graph a valid tree so there has to be more right?
        # Another important property of a tree is that it is fully connected! ie you can trace your way from any Node, starting from any Node
        # So we cant have something like this
        # A --- B       D --- E
        # |
        # C
        # Aside these 2 things.. what else do you think makes a graph a valid tree? Interestingly, the answer is nothing else!
        # These are the two main properties!. 1 that there are no cycles and 2, that it is fully connected... So we can simply check for those two!



        # To make our lives easier let's first convert the edge list into an adjacency list
        graph = defaultdict(list)
        for l, r in edges:
            # Because this is an undirected graph, we have to add to both sides
            graph[l].append(r)
            graph[r].append(l)

        visited = set()
        def hasCycle(node, parent, path):
            if node in path: return True
            if node in visited: return False

            path.add(node)

            for neighbor in graph[node]:
                # If this is the node I just came from, we can ignore it
                # Because this is an undirected graph, we already know one neighbor points back to me
                if neighbor == parent: continue
                if hasCycle(neighbor, node, path): return True

            path.remove(node)
            visited.add(node)

            return False

        cycle = hasCycle(0, -1, set())
        visitedAllNodes = len(visited) == n

        # If we didn't have a cycle, and we could visit all the nodes, then its a valid tree!
        return (not cycle) and visitedAllNodes