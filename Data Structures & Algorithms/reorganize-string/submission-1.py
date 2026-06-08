class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [[-freq, char] for char, freq in count.items()]
        heapq.heapify(heap)

        prev = None
        res = []

        while heap or prev:
            if prev and not heap:
                return ""
            
            cnt, char = heapq.heappop(heap)
            res.append(char)
            cnt += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        
        return "".join(res)

