class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Unlike our last solution where we used sorting to keep track of the two largest elements, we can use a heap! 
        # Remember what the job of a heap is.. To keep track of the biggest/smallest element
        # And after removing the top element(s), we can just heapify and that is O(logn) instead of O(nlogn)

        # Because earlier versions of python do not have a maxheap, we can use a negative minHeap
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        # We can only smash two stones if we have up to two stones!
        while len(heap) > 1:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)

            # If the two stones are the same weight, we don't need to do anything since we already popped them
            # If x is bigger than y, then we can append their diff to the heap(which will heapify again and bubble the max to the top)
            if x > y: heapq.heappush(heap, -(x-y))
        
        # If we end up with just one element in the array, return it. If not return 0
        return 0 if not heap else -heap[0]