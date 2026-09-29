class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # The last approach we took was the most intuitive one and its basically how we would have handled it as humans. 
        # ie isolate a section, verify it.. isolate the next section, verify it.... repeat etc...
        # The downside of this approach programmatically is that we walk the cells too many times.
        # First to isolate it, and then our helper walks it again to validate it... 
        # Another downside of the previous solution was that we had to write some crazy 4x for loop to get the sub boxes.
        
        # I think there is a somewhat cleaner way to do this. If we look again, we will notice that every cell is a member of a column, row and subbox... 
        # Soo this means that at each cell, we know what row, column and subbox it belongs to. 
        # Now what if we walk the board once and validate each cell along the way.

        digits = set("123456789")
        rows, cols, subboxes = defaultdict(set), defaultdict(set), defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):

                digit = board[row][col]
                if digit not in digits: continue

                # Check if its valid within its row
                if digit in rows[row]: return False
                rows[row].add(digit)

                # Check if its valid within its column
                if digit in cols[col]: return False
                cols[col].add(digit)

                # Check if its valid within its 3x3 sub box
                # This is the part we intend to use to replace that whole 4x for loop.
                # Think about this.... The boxes are just rows and columns chopped into groups of 3, and integer division is basically
                # the operation that collapses a group of 3 into one number eg if the row numbers are:
                #   row:      0 1 2 3 4 5 6 7 8
                #   then doing row // 3 gives: 0 0 0 1 1 1 2 2 2
                # So rows 0,1,2 all land on box-row 0, rows 3,4,5 on box-row 1, and so on. Same for columns.
                # When you put the two together and you get a coordinate for the box itself, eg the centre box is (1,1),
                # which we can then use as the key for that box's set
                subbox = (row//3, col//3)
                if digit in subboxes[subbox]: return False
                subboxes[subbox].add(digit)

        return True

