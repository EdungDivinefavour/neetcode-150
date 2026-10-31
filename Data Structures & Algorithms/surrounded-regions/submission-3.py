
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Another way we can approach this problem is in reverse
        # ie what if we start from the borders and check every cell that a border can reach, just like the pacific/atlantic problem
        # See https://github.com/EdungDivinefavour/neetcode-150/blob/master/Data%20Structures%20%26%20Algorithms/pacific-atlantic-water-flow/submission-1.py
        # The idea is that if we explore from the border and a border could reach that cell, then we know it for sure is an invalid region......
        # So we can just mark it as #
        # Every other O cell that we didn't mark is for sure a valid region because itself cannot find its way to a border
        #
        # Why does this work though?
        # Well, remember that a region is only valid for capture if none of its Os can reach the border
        # So instead of finding all the islands and checking if each one touches the border, why don't we just start from the borders themselves?
        # Any O we can reach from there is automatically not something we should capture
        # And if we have gone through all the bordering Os and still haven't reached a particular O, then there is no way that O is connected to the border
        # So we can safely capture it

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def explore(row, col):
            if (
                row < 0 or row >= len(board) or # Row out of bounds 
                col < 0 or col >= len(board[0]) or # Col out of bounds
                board[row][col] != "O" # If its something other than a O, we dont really care about it
            ): return

            # We actually don't need a visited set anymore because we are using the board itself to mark what we have visited
            # Once I become #, another DFS won't explore me again because I am no longer an O
            board[row][col] = "#"

            # Now lets check all my neighbors.. if they are also Os, we want to mark them too
            # Because if the border could reach me, then it can also reach any O connected to me
            for dr, dc in directions:
                explore(row+dr, col+dc)

        # First lets find all the cells that we can reach from the borders
        for r in range(len(board)):
            for c in range(len(board[r])):
                # If we meet a border cell, lets explore and see all the cells it can meet
                if (
                    r == 0 or r == len(board) - 1 or
                    c == 0 or c == len(board[0]) - 1
                ): explore(r, c)

        # Now we have marked all the cells that we know cannot be our valid regions.. so every single O left is a valid one we can capture
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # After capturing, we have to return the invalid cells to O as we saw them initally
        # We only used # temporarily to make sure we don't accidentally capture cells connected to the border
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "#":
                    board[r][c] = "O"