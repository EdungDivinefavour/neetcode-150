class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Unlike the last solution, which gives us an O(nlogn), we can use a heap!
        # Build the heap using the optimal heap building approach is O(n)
        # So after doing that, we can just pop the first k from the heap and that will be our value

        heap = [-val for val in nums]
        heapq.heapify(heap)

        # We can remove the first k from the list and return the top. But ofcourse we should negate it since we stored its negative earlier
        for i in range(k):
            top = heapq.heappop(heap)
            if i == k-1: return -top
            
        return -1