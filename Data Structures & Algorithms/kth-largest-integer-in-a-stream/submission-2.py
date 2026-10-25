class KthLargest:
    # When we think of kth largest or smallest, a few thoughts come to mind.
    # Instead of doing an O(nlogn) everytime we insert into the stream like in the last solution, we could make our add call a bit better by using a heap which would give us O(logn)!
    # Remember a heap's job is to keep track of the largest/smallest at any given time
    # However if we use a maxHeap like the last solution, we would run into a problem because we can only guarantee that the topmost element is the biggest
    # We can't guarantee where the Kth largest element is

    # But if we use a minHeap and then cap the heap size of the min heap to k, the topmost element will be the kth largest
    # If you think about it, when you add the first 3 [1, 2, 3]... after adding 5, 6, 7 a min heap that is capped at size k will keep 5 at the top
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k

        # So we can start by heapifying nums when we construct the object
        # We are using negative values to store the heap's values because older python versions do not have a max heap
        # So we can just use a negative min heap and then negate the value again when we want to return it
        self.nums = nums
        heapq.heapify(self.nums)

        # Because we have a minHeap, we want to keep removing the smaller elements(ie the ones at the top)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        # We can use heappush to add the new element which will already heapify after adding to the heap
        heapq.heappush(self.nums, val)

        # Because we have a minHeap, we want to keep removing the smaller elements(ie the ones at the top)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
        