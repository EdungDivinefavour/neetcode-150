class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # One approach we can take here is when we find a land cell, we can explore our way deep to find the closest treasure chest.
        # Note: This technically works but it takes too much time. This is because we are using DFS and this does a lot of wasted/repeated computation
        
        visited = set()
        def explore(row, col):
            # If we hit any of these invalid cases ie we go out of bounds, or we hit an already visited cell or we hit a water cell
            # We are returning infinity so that the calling function will get some insanely huge distance and everything else will definitely be smaller than it
            # We don't want to return 0 because 0 will then appear the smallest path even if we know these cases are all invalid
            if (
                row < 0 or row >= len(grid) or
                col < 0 or col >= len(grid[row]) or
                (row, col) in visited or 
                grid[row][col] == -1
            ): return float('inf')

            # When we find a treasure chest, no need to proceed, we have hit the end of what we are looking for
            if grid[row][col] == 0: return 0

            # When we find a valid land cell during our hopping, we want to mark that path as visited, so that we don't end up revisiting it during the same run
            visited.add((row, col))

            # After that, we want to explore all 4 directions
            left = explore(row, col-1)
            right = explore(row, col+1)
            top = explore(row-1, col)
            bottom = explore(row+1, col)

            # After exploring, because we are looking for the minimum distance to the closest treasure chest, we are counting me + whoever the smallest is
            distance = 1 + min(left, right, top, bottom)

            # Ofcourse we should remove me from visited incase a future run needs to also hop around past me
            visited.remove((row, col))

            return distance

            
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                # No need to explore cells that are not land
                if grid[r][c] <= 0: continue 

                distance = explore(r, c)

                # If somehow after our exploration we hit a roadblock maybe everything around the land was water, this is a possible edge case we might want to handle by ignoring
                if distance >= float('inf'): continue

                grid[r][c] = distance
