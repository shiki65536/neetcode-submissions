class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = [i for i in range(n)]
        heapq.heapify(free)
        busy = []
        count = [0]*n

        for start, end in meetings:
            duration = end - start

            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free, room)
            
            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, [end,room])
            else:
                earlist_end, room = heapq.heappop(busy)
                time = earlist_end + duration                
                heapq.heappush(busy, [time, room])
            count[room] += 1

        return count.index(max(count))
