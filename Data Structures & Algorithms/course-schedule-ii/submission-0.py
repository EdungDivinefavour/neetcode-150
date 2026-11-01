class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # We should first convert the edge list into a adjacency list to make it easier to reason through
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # Hopefully you are already familiar with topological sort(top sort for short) which basically gives us an order of nodes in a graph based on which depends on which
        # eg if you have to take course A before course B... top sort will ensure that course A is processed before course B

        # If we try to go through our courses in order of which depends on which
        # If there is a cycle ie A depends on B which depends on A which depends on B, then we cannot finish all courses.. so this question basically gets reduced to that
        # Is there a cycle or not?

        stack = []
        visited = set()

        def dfs(node, path):
            # If this node is already in the path we are exploring, we can just return False early.. We have found a cycle
            if node in path: return False

            # If we processed/visited this node before, we can return here, no need to proceed
            if node in visited: return True

            # We want to store everything in the path to see if we have a cycle along this path
            path.add(node)

            # Then add its neighbors to the callstack to proceed with the exploration
            for neighbor in graph[node]:
                if not dfs(neighbor, path): return False

            visited.add(node) # Mark this node as visited
            stack.append(node) # Add it to the result stack 
            path.remove(node) # Remove it from the visited path

            return True
            
        # We can go through all the courses we have to do and do a dfs for every node
        # We are not doing for node in graph because we may have courses that are not part of the graph
        for node in range(numCourses):
            path = set()
            if not dfs(node, path): return []

        # We are returning the stack in reverse which is the idea behind the post order DFS for topological sort
        return stack[::-1]
