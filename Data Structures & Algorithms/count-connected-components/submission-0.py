class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # This question is basically asking us to count something we've been doing for all the other graph questions
        # We can start attempting to traverse the graph and for every node in the graph, we can start traversing in DFS
        # If the entire DFS for that node finishes, then we can exit our main loop and count that as 1... and repeat the same basically for everytime we reenter our main loop

        # First lets convert the edge list into an adjacency list
        graph = defaultdict(list)
        for l, r in edges:
            # We are appending to both sides since this is an undirected graph so anytime A points to B, B also points to A
            graph[l].append(r)
            graph[r].append(l)
        
        visited = set()
        def dfs(node):
            if node in visited: return
            visited.add(node)
            for neighbor in graph[node]: 
                dfs(neighbor)

        # Then we can initialize our counter
        counter = 0

        # Now let's go through the main loop and see how many times we are able to re-enter this loop
        for node in range(n):
            # If we already visited this node during some earlier traversal, it was part of some other connection so we don't want to re-enter it
            if node in visited: continue
            
            # Now we can run our DFS on this node.. whose job will basically be to mark the nodes in its path as visited
            dfs(node) 
            counter += 1
        
        # Return counter which basically tracks how many times we had to re-enter the for loop to mark something as visited
        return counter





