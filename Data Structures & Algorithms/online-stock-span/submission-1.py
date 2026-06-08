class StockSpanner:

    def __init__(self):
        self.storage = []
        

    def next(self, price: int) -> int:
        count = 1
        for i in range(len(self.storage) - 1, -1, -1):
            if self.storage[i] <= price:
                count += 1
            else:
                break
        self.storage.append(price)
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)