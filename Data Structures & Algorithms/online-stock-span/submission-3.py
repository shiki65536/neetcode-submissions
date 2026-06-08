class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, gap = self.stack.pop()
            span += gap
        self.stack.append((price, span))
        return span
        # count = 1
        # for i in range(len(self.storage) - 1, -1, -1):
        #     if self.storage[i] <= price:
        #         count += 1
        #     else:
        #         break
        # self.storage.append(price)
        # return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)