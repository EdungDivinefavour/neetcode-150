class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # This is very similar to the islands and treasures question
        # https://github.com/EdungDivinefavour/neetcode-150/blob/master/Data%20Structures%20%26%20Algorithms/islands-and-treasure/submission-3.py

        # So I will not be explaining as much here. The key thing to keep in mind is that we are using a multisouce BFS
        # If we go level by level in BFS, we will find that
        # At the end of our exploration, whatever level was the highest will be the minimum time

        # Add our rotten fruits(initial sources) to the queue
        queue = deque()

        # Count our fresh fruits so that we can know if we corrupted them and if we have any ones left
        fresh = 0 
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))


        minutes = 0

        # Now we can start spreading the disease.
        # Unlike the last solution, we are checking if there are fresh fruits because there is no need to run the loop if there is nothing to corrupt
        while fresh > 0 and queue:
            
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

                    # Also reduce the fresh fruits that we have left
                    fresh -= 1 
                
            minutes += 1

        return -1 if fresh else minutes