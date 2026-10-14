
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # This is an interesting question and a good way to learn how to traverse boards.
        # The strategy we can use is as follows:
        # We can loop through the board and try to check if each character is our desired character. If its not, this starting point is useless and we just move on to the next character in the board
        # If we find the first character of our word, then we want to check all 4 directions of it and see if we can find the next character.
        # And when we find that character, we want to check all of its 4 directions to see if we can find the next.... and so on

        visited = set()
        def explore(row, col, index):
            # If we have matched every character in the word
            if index == len(word): return True

            # If we go out of bounds, or if we find a character that we already saw before during this run.. or if the character we land at is not the one we are looking for,
            # This direction is useless and we should consider it False ie it can't possibly be where our desired character is
            if (
                (row, col) in visited or
                row < 0 or row >= len(board) or
                col < 0 or col >= len(board[row]) or
                board[row][col] != word[index]
            ): 
                return False
                        
            # Mark this character as visited
            visited.add((row, col))

            # If this character is what im looking for, we can explore all 4 directions and see if we can find our next character
            # If this was the last character, the next call will see we've matched the whole word and return True
            directions = [(row, col-1), (row, col+1), (row+1, col), (row-1, col)]
            foundNext = False
            for dr, dc in directions:
                if explore(dr, dc, index+1): foundNext = True

            # Remove me from the visited set because this path is done with me, and another path might still need to use me
            visited.remove((row, col))

            # We want to return whether we found the next character in one of the four directions
            return foundNext
                
        for r in range(len(board)):
            for c in range(len(board[r])):
                wordExists = explore(r, c, 0)
                if wordExists: return True

        # If we come this far and we didn't return early due to finding the word, then this word does not exist in our board   
        return False