class KthLargest:
    # When we think of kth largest or smallest, a few thoughts come to mind.
    # Instead of doing an O(nlogn) everytime we insert into the stream like in the last solution, we could make our add call a bit better by using a heap which would give us O(logn)!
    # Remember a heap's job is to keep track of the largest/smallest at any given time
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k

        # So we can start by heapifying nums when we construct the object
        # We are using negative values to store the heap's values because older python versions do not have a max heap
        # So we can just use a negative min heap and then negate the value again when we want to return it
        self.nums = [-val for val in nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        # We can use heappush to add the new element which will already heapify after adding to the heap
        heapq.heappush(self.nums, -val)

        # Because a heap only guarantees us the value of the topmost element, we can't really check the kth largest so we can do some tricks
        # One I am thinking of is to make a copy of the heap(but this is not very efficient). Let's see if it works
        copy = self.nums[:]

        # And then loop through this copy and remove the head and keep heapifying
        largest = None
        for i in range(self.k):
            largest = -heapq.heappop(copy)
        
        return largest