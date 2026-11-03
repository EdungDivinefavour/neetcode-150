class Solution:
    # This is basically copied from word search 1.. See
    # https://github.com/EdungDivinefavour/neetcode-150/tree/master/Data%20Structures%20%26%20Algorithms/search-for-word
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def explore(row, col, index):
            if index == len(word): return True
            if (
                (row, col) in visited or
                row < 0 or row >= len(board) or
                col < 0 or col >= len(board[row]) or
                board[row][col] != word[index]
            ): return False
                        
            visited.add((row, col))
            directions = [(row, col-1), (row, col+1), (row+1, col), (row-1, col)]
            foundNext = False
            for dr, dc in directions:
                if explore(dr, dc, index+1): foundNext = True

            visited.remove((row, col))
            return foundNext
                
        for r in range(len(board)):
            for c in range(len(board[r])):
                wordExists = explore(r, c, 0)
                if wordExists: return True

        return False

    # Pretty sure this solution is very inefficient but just out of curiosity.. I want to see how bad the situation will be : )
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        out = []

        # Go through the words in the array
        for word in words:
            # If we find one that exists in the board, add it to the output array
            if self.exist(board, word):
                out.append(word)
        
        return out