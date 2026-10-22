class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # So we know the last solution was very inefficient and the reason it was is because, given
        # Input: [
        #     [2147483647,-1,0,2147483647],
        #     [2147483647,2147483647,2147483647,-1],
        #     [2147483647,-1,2147483647,-1],
        #     [0,-1,2147483647,2147483647]
        # ]
        # When we go from say 0,0 to 3,0.. we pass through 1,0 and 2,0.. and then we get their distance and pass it to 0,0 when we return in the call stack.
        # Now when its time for 1,0 to calculate its distance, we dig all the way deep again and recompute things we already knew as of the last time we met 1,0 and everything deep from it.
        # This is very inefficient

        # We can instead do a BFS... However, if we do a regular BFS, we will get the closest lands to a treasure(from the POV of that treasure)
        # But this would lead to a case where treasure 0,2 can modify cell 2,0 but cell 3,0 will come back and change that cell to something else.
        # This could end up happening so many times and is also very inefficient.

        # There is a trick we can apply here called Multi Source BFS where we start with all the cells we want to spread out from, loaded in a queue
        # And then start exploring from there, this helps to give all of the starting cells the same fair chance to hop one at a time.
        # No cell gets to hop far around while others are yet to hop
        # This helps to guarantee us that the first time we mark a cell, that was the shortest distance to that cell.


        # Let's store the starting cells in a queue
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    queue.append((r, c))

        
        # Now let's begin exploring from our starting cells and spreading out
        distance = 1

        # I think we can do without the discovered set we added in solution 2. 
        # If the whole point of that set was to ensure that we didn't add something that was waiting to be processed,
        # We can just use the grid itself to mark them as discovered maybe with a 
        while queue:
            for _ in range(len(queue)):
                # Get the element from the front of the queue
                row, col = queue.popleft()

                # Aside the very first time, we will always land here on a land cell, so we can set the current level as the shortest distance

                # Add the valid land cells to the queue so we can mark them later
                # If we find an invalid cell, we don't want to bother traveling from it.. so lets skip the bad ones
                directions = [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]
                for r, c in directions:
                    if (
                        r < 0 or r >= len(grid) or
                        c < 0 or c >= len(grid[0]) or
                        grid[r][c] <= 0 or
                        # If this was previously a valid land cell but we have updated with something that makes it to no longer be land
                        grid[r][c] != 2147483647
                    ):
                        continue

                    queue.append((r, c))
                    grid[r][c] = distance

            distance += 1
