class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_finish(rate: int) -> bool:
            time = 0
            for pile in piles:
                time += pile // rate
                if not pile % rate == 0:
                    time += 1
                if time > h:
                    return False
            return True

        l, r = 1, max(piles)
        boundary = -1

        while l <= r:
            mid = (l+r) // 2
            if can_finish(mid):
                boundary = mid
                r = mid - 1
            else:
                l = mid + 1

        return boundary
















        left, right = 1, max(piles)

        def hours_needed(k: int) -> int:
            total = 0
            for p in piles:
                total += (p + k - 1) // k  # ceil(p / k)
            return total
        
        while left <= right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left