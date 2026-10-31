class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # My first thought is to approach this problem like the islands problem
        # https://github.com/EdungDivinefavour/neetcode-150/blob/master/Data%20Structures%20%26%20Algorithms/count-number-of-islands/submission-0.py

        # We can think about this problem in 3 steps.
        # First we should find the regions (basically islands)...Second we can check that it is surrounded... and Lastly we can capture it!
        visited, regionCells = set(), set()

        def explore(row, col, candidates):
            if(
                row < 0 or row >= len(board) or # Row out of bounds
                col < 0 or col >= len(board[0]) or # Col out of bounds
                (board[row][col] == "O" and (row == 0 or row == len(board) - 1)) or # Is a bordering O row
                (board[row][col] == "O" and (col == 0 or col == len(board[0]) - 1)) # Is a bordering O column
            ): return False

            # If we hit an X it is still technically desired ie it doesnt tell us that we have to abort immediately
            # Also the fact that we have visited a cell before shouldn't be grounds to destroy the entire DFS
            # If it has already been visited during this run
            if (row, col) in visited or board[row][col] == "X": return True

            # Mark me as visited because we don't need to ever use me again
            visited.add((row, col))

            # We can collect candidate cells, we don't want to capture it yet since we don't know how it will all end.. ie if it will become a fully valid region at the end
            candidates.add((row, col))

            # At this point, I am both a desired O cell and also not a border, so we only want to verify my neighbors are all desired and not bordering Os

            left = explore(row, col-1, candidates)
            right = explore(row, col+1, candidates)
            top = explore(row-1, col, candidates)
            bottom = explore(row+1, col, candidates)

            # We don't want to assume that because one cell was valid, it means the entire region was valid. So we don't add it yet to regioncells even if all 4 returned True
            # board=[
            #     ["X", "O", "O", "O", "X"],
            #     ["X", "O", "X", "O", "X"],
            #     ["X", "O", "X", "O", "X"],
            #     ["X", "X", "X", "X", "X"]
            # ]
            # This route is only valid if I was valid and all my neighbors were also valid
            return left and right and top and bottom
            
        # Start searching for potential islands
        for r in range(len(board)):
            for c in range(len(board[r])):
                # If we meet an O or we already visited it.. we can skip that
                if board[r][c] != "O" or (r, c) in visited: continue

                # We want to hold the potential candidate cells from an exploration and see if the full exploration comes back as valid
                candidates = set()

                isFullyValidRegion = explore(r, c, candidates)
                if isFullyValidRegion: regionCells.update(candidates)
        
        # Capture all the region cells
        for r, c in regionCells:
            board[r][c] = "X"