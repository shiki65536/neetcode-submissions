class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(limit: int) -> bool:
            count = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > limit:
                    count += 1
                    curr_sum = num
                else:
                    curr_sum += num

            return count <= k

        l, r = max(nums), sum(nums)

        while l <= r:
            mid = (l + r) // 2

            if can_split(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l