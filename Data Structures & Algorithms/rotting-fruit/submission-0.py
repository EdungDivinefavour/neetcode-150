class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # This is very similar to the islands and treasures question
        # https://github.com/EdungDivinefavour/neetcode-150/blob/master/Data%20Structures%20%26%20Algorithms/islands-and-treasure/submission-3.py

        # So I will not be explaining as much here. The key thing to keep in mind is that we are using a multisouce BFS
        # If we go level by level in BFS, we will find that
        # At the end of our exploration, whatever level was the highest will be the minimum time

        # Add our rotten fruits(initial sources) to the queue
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r, c))

        # Now we can start spreading the disease
        minutes = -1
        while queue:

            # We want to lock in the current elements in the queue since we will be mutating the queue along the way
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                # Set all 4 directions we want to explore
                directions = [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]

                for dr, dc in directions:

                    # There are some cells we don't really care about like the empty ones, or the ones we already visited or out of bound cells
                    # So we should skip them
                    if (
                        dr < 0 or dr >= len(grid) or
                        dc < 0 or dc >= len(grid[0]) or
                        grid[dr][dc] == 0 or
                        grid[dr][dc] == 2
                    ):
                        continue

                    # Corrupt the cell near me and append them for the next processing
                    grid[dr][dc] = 2
                    queue.append((dr, dc))
                
            minutes += 1


        flattened = {item for row in grid for item in row}
        return (
            # If we still have fresh fruits left return -1
            -1 if 1 in flattened else 

            # If there were no rotten fruits initially, the loop would have never ran so minutes is still -1. 
            # If there were rotten fruits at the start but no fresh ones, the loop would have ran once, making minutes 0.
            # In both cases, no rotting was needed, so we would return 0.
            max(0, minutes)
        )
