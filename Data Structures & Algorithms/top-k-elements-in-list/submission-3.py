class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))

            if k < len(heap):
                heapq.heappop(heap)
        
        return [x[1] for x in heap]

        # counter = Counter(nums)
        # sorted_counter = dict(sorted(counter.items(),  key=lambda x:x[1], reverse=True))
        # return list(sorted_counter.keys())[:k]
















        # freq = defaultdict(int)
        # for num in nums:
        #     freq[num] += 1

        # heap = []

        # for num, count in freq.items():
        #     heapq.heappush(heap, (count, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap) 
        # return [num for count, num in heap]