class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # We first want to convert this edge list to an adjacency list to make our lives easier
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        # If you think about what would cause a redundant connection in a graph, it would be the presence of a cycle!
        # How do we know we have a cycle? It is basically the fact that we initially added an additional edge that pointed to two existing vertices.
        # So once we find a cycle, we have found the redundancy because that is the only time that we don't need to have two nodes connected to each other.
        # Because that is the first time that we will have a connection that we don't really need(redundant!)
        # Once we find our cycle, we want to find the last edge element that formed the cycle and return that.

        visited, cycle = set(), set()
        path, pathSet = [], set() # pathSet is basically same as path, just keeps track of the same thing so we can check in O(1 time)
        
        def detectAndStoreCycle(node, parent):
            if node in pathSet:
                # Once we find a node that was repeated, we must have earlier added it to the path So that Node must be the start of the cycle!
                # But you see if we had [1, 2, 3, 4, 2], 2 would have been reported as the start of the cycle, 
                # But inside our path, we have 1 there since thats where we may have started our dfs from
                # So we need to remove the nodes that are not part of the cycle when we want to store what the cycle is.
                # Because our path list stored the elements in order, every element before the first occurence of 2 is not part of our cycle 
                cycleStartPos = path.index(node)
                cycle.update(path[cycleStartPos:])
                return True

            if node in visited: return False
            
            path.append(node)
            pathSet.add(node) # Track that this node is part of the current active recursion branch
            
            for neighbor in graph[node]:
                if neighbor == parent: continue
                if detectAndStoreCycle(neighbor, node): return True
                
            path.pop()
            pathSet.remove(node) # Backtrack from the current active path once the node's neighbors are fully checked

            visited.add(node)
            return False
            
            
        detectAndStoreCycle(1, -1)

        # Every edge on the cycle at this point is a potential candidate, but we want the one that appears last in the input
        # So we can walk edges from the back, and the first edge with both of its ends on the cycle is our answer
        for i in range(len(edges)-1, -1, -1):
            x, y = edges[i]
            if x in cycle and y in cycle:
                return [x, y]
        
        return []