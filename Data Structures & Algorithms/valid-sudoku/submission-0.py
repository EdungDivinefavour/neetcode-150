class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # The board has 3 rules and you will notice that each one is really the same question asked about a different group of 9 cells
        # Which is:
        # Are there any repeated digits in this section? So if we can answer that for one group of 9, we can answer the whole problem
        # I would consider this approach the collecting approach.. in the sense that we gather each group into a list first, then hand it off to be checked.
        # The rows come for free since the board is already a list of rows, columns we can get by zipping,
        # and the boxes we have to walk out by hand since nothing in the structure groups them for us.
        # The tradeoff is that we end up passing over the board 3 separate times, once per rule




        digits = ("123456789")
        # Convienience function to verify each section... we can run our rows, columns and the subboxes through this method
        def isSectionValid(section: List[str]) -> bool:
            A, numCount = set(), 0
            for num in section:
                if num in digits: # We are doing this because we don't really care about the dots in the array
                    numCount += 1
                    A.add(num)
            return len(A) == numCount # If the set has the same number of elements as the count of numbers

        # Let's verify rule number 1
        for row in board:
            if not isSectionValid(row): return False # If any row is not valid, the entire board is not valid so return early

        # Let's verify rule number 2
        for column in zip(*board):
            if not isSectionValid(column): return False # Similarly, if any column is not valid, the entire board is not valid so return early
        
        # Now onto the interesting part, let's verify rule number 3
        # If we think carefully, we will find that the only thing that separates one box from another is where its top-left corner sits,
        # and those corners only ever land on 0, 3 or 6 in either direction.. so we can just generate all 9 pairs
        for startRow in range(0, 9, 3):
            for startCol in range(0, 9, 3):
                section = [] # We want to make a fresh list per box, otherwise the previous box's numbers will slip into this one
                for r in range(startRow, startRow + 3):
                    for c in range(startCol, startCol + 3):
                        section.append(board[r][c])

                # When we have all 9 cells in the box, we can check if that box is valid. We want to check once all 9 cells are in, not while we are still filling it
                if not isSectionValid(section): return False
        
        return True