class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        char_set = set()

        for num in nums:
            if num in char_set:
                return num
            else:
                char_set.add(num)