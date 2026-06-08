class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers, 1):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            else:
               seen[num]  = i
        
        