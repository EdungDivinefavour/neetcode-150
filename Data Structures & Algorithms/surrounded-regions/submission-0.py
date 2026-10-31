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

            # One issue with this solution is that we are assuming that because I am an O and I am not bordering, then I am a valid region cell
            # But that is not necessarily true.. I could still be connected to another O that touches the border
            # Also we are adding me to regioncells before we have even checked my neighbors.. ie we don't know yet if this entire region is actually surrounded

            # For example:
            # board = [
            #     ["X", "O", "X"],
            #     ["X", "O", "X"],
            #     ["X", "X", "X"]
            # ]
            #
            # When we explore (1,1), we add it to regioncells because it is an O and it is not on the border
            # But when we explore its top neighbor (0,1), we realize that it is a bordering O
            # At that point, we just return.. but we have already added (1,1) to regioncells
            # And nothing tells us that we should remove it because its region is no longer valid
            # So when we eventually capture all our regioncells, (1,1) will incorrectly become X
            #
            # Another issue is that even if we tried checking that all my neighbors were valid before adding me
            # It still wouldn't necessarily mean that the entire region is valid
            # A child could return successfully, but its parent might later discover another path that reaches the border
            # At that point, it would already be too late because the child has returned and added itself to regioncells
            #
            # So we shouldn't assume that because one cell is valid, the entire region is valid
            # We need to first finish checking the region before deciding whether its cells should be captured

            explore(row, col-1)
            explore(row, col+1)
            explore(row-1, col)
            explore(row+1, col)

            visited.remove((row, col))

            # Another issue is that we are removing me from visited
            # But why would we want to explore me again if we have already processed me?
            # This is not like a backtracking problem where another path might need to use me again
            # We are just trying to find the islands.. so once we have visited a cell, we don't need to visit it again
            # Removing me means that another DFS can end up exploring me again even though we have already done that work

        # Start searching for potential islands
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != "O": continue
                explore(r, c)

        # Capture all the region cells
        for r, c in regioncells:
            board[r][c] = "X"
