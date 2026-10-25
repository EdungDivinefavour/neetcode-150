class KthLargest:
    # When we think of kth largest or smallest, a few thoughts come to mind.
    # We can try a few thing but the most intuitive way would probably be to sort the stream
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums) # Eg [1, 2, 3, 3]

    def add(self, val: int) -> int:
        # When we add a new element to the stream, we can sort the stream
        # eg if we append 5, 3, 6, 7, 8 the stream becomes [1, 2, 3, 3, 3, 5, 6, 7, 8]
        self.nums.append(val)
        self.nums = sorted(self.nums)

        # Then return the kth element from the back from the stream
        return self.nums[-self.k]