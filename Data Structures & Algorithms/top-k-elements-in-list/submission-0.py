class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = defaultdict(int)
        for num in nums:
            record[num] += 1
        print(sorted(record.items()))
        sorted_record = sorted(record.items(), key=lambda x:x[1], reverse=True)

        return [key for key, value in sorted_record][:k]