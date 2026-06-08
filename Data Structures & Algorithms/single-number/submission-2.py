class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
        # hash_set = set()

        # for num in nums:
        #     if num not in hash_set:
        #         hash_set.add(num)
        #     else:
        #         hash_set.remove(num)

        # return hash_set.pop()