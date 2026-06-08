class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        stack = []
        for count, ch in [(a, "a"), (b, "b"), (c, "c")]:
            if count > 0:
                heapq.heappush(heap, [-count, ch])


        while heap:
            num_cur, letter_cur = heapq.heappop(heap)
            if num_cur == 0:
                break
            if len(stack) >= 2:
                prev1 = stack[-1]
                prev2 = stack[-2]
                if letter_cur == prev1 == prev2:
                    if heap:
                        num_prev, letter_prev = heapq.heappop(heap)
                        stack.append(letter_prev)
                        num_prev += 1
                        if num_prev != 0:
                            heapq.heappush(heap, [num_prev, letter_prev])
                        heapq.heappush(heap, [num_cur, letter_cur])
                    else:
                        break
                else:
                    stack.append(letter_cur)
                    num_cur += 1
                    if num_cur != 0:
                        heapq.heappush(heap, [num_cur, letter_cur])
            else:
                stack.append(letter_cur)
                num_cur += 1
                if num_cur != 0:
                    heapq.heappush(heap, [num_cur, letter_cur])

        return "".join(stack)

