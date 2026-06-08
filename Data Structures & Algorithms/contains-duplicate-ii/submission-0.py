class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for l in range(len(nums)-1):
            r = l+1
            while r - l <= k and r <= len(nums)-1:
                if nums[l] == nums[r]:
                    return True
                else:
                    r += 1
        return False