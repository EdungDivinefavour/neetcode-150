class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # By now you are hopefully used to the idea that when we want to find the kth largest or smallest anything, we should be thinking of a heap
        # Since we are looking for the closest element to the origin, we want the smallest computed distances
        # So we can use a minHeap to store the distances such that the smallest is always at the top of the heap
        heap = []
        for i in range(len(points)):
            point = points[i]
            x, y = point[0], point[1] # Unpack the x,y values so we can use them for calculating the distance

            # The standard formula is sqrt((x1 - x2)^2 + (y1 - y2)^2)) but x2 and y2 are 0,0 since we are calculating the distance to the origin
            distance = math.sqrt((x)**2 + (y)**2)

            # We dont want to just store the distance, we also need to know which element has that distance.
            # So that when we are popping from the heap, we can know what point to append to our output array
            heapq.heappush(heap, (distance, i))
        
        output = []
        for _ in range(k):
            distance, index = heapq.heappop(heap)
            output.append(points[index])
        
        return output