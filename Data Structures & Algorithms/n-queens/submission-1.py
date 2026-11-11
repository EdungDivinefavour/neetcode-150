class Solution:
    # Compared to the last solution, we don't really need the rows set because our backtracking solution is only looking at each row once when trying a combo

    def solveNQueens(self, n: int) -> List[List[str]]:
        # This is a very famous Leetcode problem and is usually considered a scary one but it's actually not that hard once you give it some thought.
        # First thing we have to keep in mind is that, in real chess, given say 4 queens, we can indeed place say only 2 queens such that the board becomes locked and we can't place any more. eg
        # Q . . .
        # . . Q .
        # . . . .
        # . . . .
        # The N queens problem is not asking us to find all placements of the queens, it is asking us to find all placements such that "ALL N" queens are successfully placed on the board!
        # So, if we encounter the placement above, while it's technically a valid chess move, it is not a desired N queens placement, so we have to reject it because it couldn't help us place all N queens.
        # With that in mind, let's solve the actual problem...................
        # So we want to place "all N" queens on an N by N board and we don't want them to attack each other.
        # For a queen to attack another queen, they have to be on the same row. Or column. Or diagonal right?
        # So because we are trying to place all N queens, we must ensure that when we use a row, no queen ever enters that row again... same with a column and same with a diagonal
        # This means, we kinda found our approach already! We can simply brute force our way into placing the queens and then store what columns and diagonals have been occupied by some other queen.
        # We don't need to store rows, because we only ever place one queen per row as we move down the board
        # One more thing I should mention is how we can get a diagonal.. for any given cell, it will have 2 diagonals.. positive(/) and negative(\)
        # Let's say you are at [3][0], and we want to know how to spot a cell along its positive diagonal. 
        # You will notice that for all the cells along its positive diagonal, [2][1], [1][2], [0][3], there is a pattern! They all sum to 3+0 ie 3
        # So this means that when we find a given cell, no queen should ever be placed on a cell with posD of r+c!
        # It's the exact same story with negative diagonal, just that it's r-c this time
        

        cols, posD, negD = set(), set(), set()
        board = [["."] * n for _ in range(n)] # We can start out by using an N x N board filled with dots 
        out = []

        def placeQueens(r):
            if r == n:
                # Store the valid board combo we found but remember we want to return the output as [[".Q..", "...Q" etc etc]]
                copy = ["".join(row) for row in board] 
                out.append(copy)
                return
         
            for c in range(len(board[r])):
                if c in cols or r+c in posD or r-c in negD: continue

                # If the above check doesn't fail, we have found a potential valid column placement for that row.
                # So let's place a Queen at this cell, then store this col and its diagonals in our sets so that nothing tries to place a queen there
                cols.add(c)
                posD.add(r+c)
                negD.add(r-c)
                board[r][c] = "Q"

                # Now that we found a potentially valid column placement for that row, eg [.Q..].. We need to know all the other possible column placements we can make from this exact point ie having locked this row/col combination so far.
                
                # To do this, we have to try placing queens in the next available row from here, which will go on to check all valid columns it can do from there.. and so on
                placeQueens(r+1)

                # If this placement combination ends up being valid, it will at some point hit r == n. ie the base case above, which will store our fully valid board combo.

                # If it is not valid, then at some point we will reach a row where every single column is already attacked by a queen we placed earlier.. so the continue above skips all of them and the for loop ends without placing anything
                # When that happens, that call will just return, and we are back here in the previous row, where we backtrack and move on to try its next column

                # Anyway, after all of this is done, we need to backtrack and free things up for the next column so it can have its own try.. Who knows how many columns can lead to a valid placement.

                # To backtrack, we just need to remove everything from our sets and of course set the cell back to a .
                cols.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
                board[r][c] = "."

        # We are not doing placeQueens(0, 0) because we know that for all rows, we will look at every single column. 
        # So we only need to pass the row we are starting at and don't need to care to pass the column
        placeQueens(0)
        return out