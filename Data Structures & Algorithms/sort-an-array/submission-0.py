class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []

        heap = []

        for num in nums:
            heapq.heappush(heap, num)

        while heap:
            num = heapq.heappop(heap)
            res.append(num)

        return res
            
