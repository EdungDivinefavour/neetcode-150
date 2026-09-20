class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # A brute force solution would be to do an O(n^2) search through the matrix
        # We could do better... What if we do a pass through the rows and then for each row, we perform a binary search.
        # That will give us an O(m) * O(logn) solution which is much better
        # We can make an improvement to our last solution... The question says that the first element is greater than the last element in the previous row
        # This means we can skip a lot of things .eg,

        for row in matrix:
            # If the biggest element ie last element in the row is smaller than our target... our target cannot exist in that row, so we can just skip the row
            if row[-1] < target: continue

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