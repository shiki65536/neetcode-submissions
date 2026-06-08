class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = [[frm, to, num, 0] for num, frm, to in trips]
        heapq.heapify(heap)
        seated = 0 
        while heap:
            f, t, n, b = heapq.heappop(heap)
            if b == 0:
                seated += n
                if seated > capacity:
                    return False
                
                heapq.heappush(heap, [t,t,n,1])
            else: #  b == 1
                seated -= n
        
        return True