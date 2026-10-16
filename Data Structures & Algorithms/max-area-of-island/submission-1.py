class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # This question shares a lot of similarities with the numberOfIslands question so I won't be explaining as much
        # https://github.com/EdungDivinefavour/neetcode-150/tree/master/Data%20Structures%20%26%20Algorithms/count-number-of-islands

        maxArea, visited = 0, set()

        # The key difference here is that we want to count all the cells that make up the island
        def explore(row, col):
            if (
                row < 0 or row >= len(grid) or
                col < 0 or col >= len(grid[0]) or
                (row, col) in visited or
                grid[row][col] == 0
            ): return 0

            # If this is a valid cell, lets mark it as visited
            visited.add((row, col))

            area = 1 # Count me first
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for dr, dc in directions:
                area += explore(row+dr, col+dc) # Count what we can find in all 4 directions

            return area


        for r in range(len(grid)):
            for c in range(len(grid[r])):
                # We should update maxArea with whatever we found during our latest exploration
                maxArea = max(maxArea, explore(r, c))

        return maxArea