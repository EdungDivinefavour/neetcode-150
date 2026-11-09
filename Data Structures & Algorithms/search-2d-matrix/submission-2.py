class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # A brute force solution would be to do an O(n^2) search through the matrix
        # We could do better... What if we do a pass through the rows and then for each row, we perform a binary search.
        # That will give us an O(logmn) solution which is much better
        # We can make an improvement to our last solution... The question says that the first element is greater than the last element in the previous row


        # So think about what that means.. if every row starts bigger than the last one ended, then the whole matrix is basically one big sorted array that has just been cut into rows
        # So we don't need to find the row first at all.. we can just pretend the matrix is one long sorted array and do a single binary search on it
        # The cool thing is.. We don't even actually need to build that array, we can just pretend it is there. 
        # ie It would have ROWS * COLS elements, so the indices go from 0 to ROWS * COLS - 1
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        
        while l <= r:
            m = l + (r - l) // 2

            # After we compute m, the only catch is that we can't do matrix[m].. because m is an index in our pretend long array
            # So we need to convert it back to a row and a col. Every row has COLS elements, so m // COLS tells us how many full rows we skipped and m % COLS tells us how far into that row we are
            row, col = m // COLS, m % COLS
            
            # If the target is bigger than the middle, everything to the left of it is useless, so we can search the right half
            if target > matrix[row][col]:
                l = m + 1
            
            # If the target is smaller than the middle, then everything to the right of it is useless, so we can search the left half
            elif target < matrix[row][col]:
                r = m - 1
            else: 
                return True
        
        # If l crossed r and we never found it, then the target is not in the matrix
        return False