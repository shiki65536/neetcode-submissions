class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n - 2):
            if nums[i] > 0:
                break  # 後面都 >= nums[i]，不可能湊到 0

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # i 去重

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # l 去重
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # r 去重
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return res
        