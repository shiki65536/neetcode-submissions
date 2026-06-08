class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """ confirm duplucation """

        # Error Handling: 
        ## 1. empty
        ## 2. Invalid
        if not nums:
            return False
        
        # Logic
        ## set
        nums_set = set(nums)

        return not len(nums_set) == len(nums)




