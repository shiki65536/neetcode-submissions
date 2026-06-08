class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = {}
        output = []

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            if count[num] > n//3:
                if num not in output:
                    output.append(num)
        
        return output