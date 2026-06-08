class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        val = self.stack[-1]
        return val
        

    def getMin(self) -> int:
        val = self.min[-1]
        return val
        
