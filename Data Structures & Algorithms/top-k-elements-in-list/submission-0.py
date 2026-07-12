class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A = {}
        for num in nums:
            A[num] = 1 + A.get(num, 0)
        
        arr = [(-v, k) for k, v in A.items()]
        heapq.heapify(arr)

        res = []
        for i in range(k):
            top = heapq.heappop(arr)
            res.append(top[1])
        
        return res

