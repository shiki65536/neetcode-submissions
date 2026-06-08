class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        l = 0
        for r in range(len(people)-1, -1, -1):
            if r < l:
                break
            if people[r] + people[l] <= limit:
                    l += 1
            count += 1

        return count
