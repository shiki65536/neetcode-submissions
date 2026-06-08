class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def under_k(limit: int):
            cur_sum = 0
            count = 1
            for num in nums:
                if cur_sum + num > limit:
                    count += 1
                    cur_sum = num
                else:
                    cur_sum += num
            
            return count <= k

        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l + r) // 2

            if under_k(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l