class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # My first thought is to approach this problem like the islands problem
        # https://github.com/EdungDivinefavour/neetcode-150/blob/master/Data%20Structures%20%26%20Algorithms/count-number-of-islands/submission-0.py

        # We can think about this problem in 3 steps.
        # First we should find the regions (basically islands)...Second we can check that it is surrounded... and Lastly we can capture it!
        if not board or not board[0]: return

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        visited, regionCells = set(), set()

        def explore(row, col, candidates):
            stack = [(row, col)]
            isFullyValidRegion = True

            while stack:
                row, col = stack.pop()

                if(
                    row < 0 or row >= len(board) or # Row out of bounds
                    col < 0 or col >= len(board[0]) or # Col out of bounds
                    (board[row][col] == "O" and (row == 0 or row == len(board) - 1)) or # Is a bordering O row
                    (board[row][col] == "O" and (col == 0 or col == len(board[0]) - 1)) # Is a bordering O column
                ):
                    # This region is no longer valid since we have encountered a bordering O
                    isFullyValidRegion = False
                    continue

                # If we hit an X it is still technically desired ie it doesnt tell us that we have to abort immediately
                # Also the fact that we have visited a cell before shouldn't be grounds to destroy the entire DFS
                # If it has already been visited during this run
                if (row, col) in visited or board[row][col] == "X": continue

                # Mark me as visited because we don't need to ever use me again
                visited.add((row, col))

                # We can collect candidate cells, we don't want to capture it yet since we don't know how it will all end.. ie if it will become a fully valid region at the end
                candidates.add((row, col))

                # At this point, I am both a desired O cell and also not a border, so we only want to verify my neighbors are all desired and not bordering Os
                for dr, dc in directions:
                    stack.append((row + dr, col + dc))

            # We don't want to assume that because one cell was valid, it means the entire region was valid. So we don't add it yet to regioncells even if all 4 returned True
            # board=[
            #     ["X", "O", "O", "O", "X"],
            #     ["X", "O", "X", "O", "X"],
            #     ["X", "O", "X", "O", "X"],
            #     ["X", "X", "X", "X", "X"]
            # ]
            # This route is only valid if I was valid and all my neighbors were also valid
            # With iterative DFS, we don't have individual return values from neighbors anymore
            # Instead we only return True if we never encountered a bordering O during this entire run
            return isFullyValidRegion

        # Start searching for potential islands
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != "O" or (r, c) in visited: continue

                candidates = set()
                isFullyValidRegion = explore(r, c, candidates)

                if isFullyValidRegion: regionCells.update(candidates)

        # Capture all the region cells
        for r, c in regionCells:
            board[r][c] = "X"