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

        # We can eliminate the need for the stack and use a direct output array instead
        output = [0] * numCourses 
        index = numCourses - 1
        visited = set()

        def dfs(node, path):
            nonlocal index
            # If this node is already in the path we are exploring, we can just return False early.. We have found a cycle
            if node in path: return False

            # If we processed/visited this node before, we can return here, no need to proceed
            if node in visited: return True

            # We want to store everything in the path to see if we have a cycle along this path
            path.add(node)

            # Then add its neighbors to the callstack to proceed with the exploration
            for neighbor in graph[node]:
                if not dfs(neighbor, path): return False

            path.remove(node) # Remove it from the visited path
            visited.add(node) # Mark this node as visited
            
            output[index] = node # Add it to the back of the output list
            index -= 1 # Reduce index so the next element can add to the next available spot

            return True
            
        # We can go through all the courses we have to do and do a dfs for every node
        # We are not doing for node in graph because we may have courses that are not part of the graph
        for node in range(numCourses):
            path = set()
            if not dfs(node, path): return []

        # We can return that output array which is basically the post order DFS + our adding it from the back
        return output
