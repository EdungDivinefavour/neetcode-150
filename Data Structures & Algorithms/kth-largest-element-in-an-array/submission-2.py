class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We can even further clean up our heap solution by using a min heap instead
        # The idea being that in a minheap with max size k, the topmost element will always be the kth largest
        # Imagine if we have [1, 2, 3, 4, 5, 6, 7, 8] and k = 3 .. If we can the minheap at size 3, it will be [6, 7, 8] so 6 will be the one at the top

        heap = [val for val in nums]
        heapq.heapify(heap)

        # Keep trimming the heap until we only have k elements in the heap
        while len(heap) > k: heapq.heappop(heap)

        # Return the topmost element in the heap
        return heap[0]