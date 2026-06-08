class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        sorted_count = sorted(count.items(), key=lambda x:x[1], reverse=True)

        return sorted_count[0][0] 