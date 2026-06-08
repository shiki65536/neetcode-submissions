class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            weight = abs(num - x)
            heapq.heappush(heap,(weight, num))
        
        res = []
        for _ in range(k):
            w, num = heapq.heappop(heap)
            print(w, num)
            res.append(num)
        res.sort()
        return res