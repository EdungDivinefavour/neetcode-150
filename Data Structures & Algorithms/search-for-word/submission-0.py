
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # This is an interesting question and a good way to learn how to traverse boards.
        # The strategy we can use is as follows:
        # We can loop through the board and try to check if each character is our desired character. If its not, we just exit early
        # If we find the first character of our word, then we want to check all 4 directions of it and see if we can find the next character.
        # And when we find that character, we want to check all of its 4 directions to see if we can find the next.... and so on

        visited = set()
        def explore(row, col, index):
            # If we go out of bounds, or if we find a character that we already saw before during this run,
            # This direction is useless and we should consider it False ie it can't possibly be where our desired character is
            if (
                (row, col) in visited or
                row < 0 or row >= len(board) or
                col < 0 or col >= len(board[row])
            ): 
                return False
            
            # If this character is not what im looking for, exit early.. no need to explore further
            if board[row][col] != word[index]: return False
            
            # If this character is what im looking for
            # But it is also the last character, no need to keep eploring other directions
            if index == len(word) - 1: return True

            # Mark this character as visited
            visited.add((row, col))

            # If this character is what im looking for and we still have more characters to find
            # We can explore all 4 directions and see if we can find our next character
            left = explore(row, col-1, index+1)
            right = explore(row, col+1, index+1)
            top = explore(row-1, col, index+1)
            bottom = explore(row+1, col, index+1)

            # Remove me from the visited set as we have explored me
            visited.remove((row, col))

            # We want to return the fact that we found me(since we made it this far)
            # But we also want to return whether we found the next character in one of the four directions
            return True and (left or right or top or bottom)
                
        for r in range(len(board)):
            for c in range(len(board[r])):
                wordExists = explore(r, c, 0)
                if wordExists: return True

        # If we come this far and we didn't return early due to finding the word, then this word does not exist in our board   
        return False
