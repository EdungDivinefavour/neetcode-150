class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Imagine you were trying to spot the islands as yourself and not the computer, what would you do?
        # When you find a 1, you would look in all 4 directions(left, top, right, bottom) to see if you can find any other connecting 1s
        # if you find a 1, in some direction, you keep looking. 
        # You would only stop considering the 1s as part of an island if you can't find any 1s in any of the 4 directions right?
        # That's exactly what we are going to do here!

        islands, visited = 0, set()

        def explore(row, col):
            # The fact that we are exploring in multiple directions means that we could go out of bounds, so we want to check for that
            # One other thing we want to check for is if we have already counted a node, we shouldn't explore it again

            if (
                row < 0 or row >= len(grid) or
                col < 0 or col >= len(grid[0]) or
                (row, col) in visited or
                grid[row][col] == "0"
            ):
                return 0
            
            # If we got this far, we found a 1 during our exploration.. What do we want to do from here?
            visited.add((row, col)) # Consider me as visited

            # Then, we should scan all four directions and see how much deeper we can go(dfs)
            # We don't care too much about whatever these four return, because they are all part of the same island we are already counting
            # We can slightly optimize our last solution.. ie since we are doing the same thing multiple times.. that sounds like a loop's job to me.
            # Also in case we wanted to cover more directions in the future
            directions = [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]
            for dr, dc in directions: explore(dr, dc)

            # When we are done exploring all four directions, we can just consider aaaaaalll of that as 1 island hence the return below
            return 1

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                islands += explore(r, c)

        return islands