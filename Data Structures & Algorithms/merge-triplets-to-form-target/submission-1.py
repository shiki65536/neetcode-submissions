class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        got0 = got1 = got2 = False
        t0, t1, t2 = target

        for a, b, c in triplets:
            # triplet cannot exceed target in any dimension
            if a > t0 or b > t1 or c > t2:
                continue

            if a == t0:
                got0 = True
            if b == t1:
                got1 = True
            if c == t2:
                got2 = True

            if got0 and got1 and got2:
                return True

        return got0 and got1 and got2

