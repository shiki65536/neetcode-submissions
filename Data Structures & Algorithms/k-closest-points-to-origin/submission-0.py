class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        def calculator(x, y):
            return x**2 + y**2
        
        for x, y in points:
            dist = calculator(x, y)
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = [[x, y] for dis, x, y in heap]
        return res