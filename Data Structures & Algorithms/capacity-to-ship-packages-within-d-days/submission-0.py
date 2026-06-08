class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l+r) // 2

            total = 0
            count = 1
            for weight in weights:
                if total + weight <= mid:
                    total += weight 
                else: # smaller mid more count
                    total = weight
                    count += 1

            if count <= days:
                r = mid 
            else:
                l = mid + 1
            print(l, r)
        
        return r
