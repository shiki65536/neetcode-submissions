class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        bucket = [[] for _ in range(len(nums)+1)]
        for num, count in freq.items():
            bucket[count].append(num)

        res = []
        for count in range(len(bucket) - 1, -1, -1):
            for num in bucket[count]:
                res.append(num)
                if len(res) == k:
                    return res