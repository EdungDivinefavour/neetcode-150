class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Hopefully you are already familiar with topological sort(top sort for short) which basically gives us an order of nodes in a graph based on which depends on which
        # eg if you have to take course A before course B... top sort will ensure that course A is processed before course B

        # If we try to go through our courses in order of which depends on which
        # If there is a cycle ie A depends on B which depends on A which depends on B, then we cannot finish all courses.. so this question basically gets reduced to that
        # Is there a cycle or not?

        # We should first convert the edge list into a adjacency list to make it easier to reason through
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # We use visited to mark the courses we have fully checked already
        visited = set()

        # We also pass a path set to mark from where we started in this run till where we are now
        def dfs(node, path):
            # If we came back to a course that is already on our path.. we found a cycle!
            if node in path: return False

            # Either we checked this one already, or nothing depends on it so it cant be part of a cycle
            if node in visited or node not in graph: return True

            path.add(node)

            for neighbor in graph[node]: 
                if not dfs(neighbor, path): return False
            
            # This means that the path was safe and no cycle came out of it so we can remove it from path and mark it as done so we don't accidentally revisit it later
            path.remove(node)
            visited.add(node)

            return True

        # The graph can be made up of a few separate pieces that don't connect to each other so we have to start from every node
        for node in graph:
            path = set()
            if not dfs(node, path): return False

        # If we got this far, then there was no cycle, so we can finish all courses
        return True