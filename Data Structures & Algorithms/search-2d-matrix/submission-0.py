class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # A brute force solution would be to do an O(n^2) search through the matrix
        # We could do better... What if we do a pass through the rows and then for each row, we perform a binary search.
        # That will give us an O(m) * O(logn) solution which is much better

        for row in matrix:
            l, r = 0, len(row) - 1

            while l <= r:
                mid = l + (r - l)//2

                if row[mid] < target:
                    l += 1
                elif row[mid] > target:
                    r -= 1
                else:
                    return True
        
        return False