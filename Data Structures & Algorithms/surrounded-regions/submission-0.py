class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Let's think about this problem like the islands problem
        # https://github.com/EdungDivinefavour/neetcode-150/blob/master/Data%20Structures%20%26%20Algorithms/count-number-of-islands/submission-0.py

        # We can think about this problem in 3 steps.
        # First we should find the regions (basically islands)
        # Second we can check that it is surrounded
        # Lastly we can capture it!

        visited, regioncells = set(), set()
        def explore(row, col):
            # I think this if statement can be simplified. Just writing it this way for clarity in the first solution
            # This is basically checking if rc is out of bounds or at the border wall or already visited
            if(
                row < 0 or row >= len(board) or # Row out of bounds
                col < 0 or col >= len(board[0]) or # Col out of bounds
                (row, col) in visited or # Already been visited during this run
                board[row][col] == "X" or
                row == 0 or row == len(board) - 1 or # Is a bordering row
                col == 0 or col == len(board[0]) - 1 # Is a bordering column
            ): return

            # At this point, we know i am valid for this region
            visited.add((row, col))
            regioncells.add((row, col))

            explore(row, col-1)
            explore(row, col+1)
            explore(row-1, col)
            explore(row+1, col)

            visited.remove((row, col))

        # Start searching for potential islands
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != "O": continue
                explore(r, c)
        
        # Capture all the region cells
        for r, c in regioncells:
            board[r][c] = "X"


