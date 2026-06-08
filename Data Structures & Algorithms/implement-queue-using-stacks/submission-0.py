class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if len(self.stack_out) == 0:
            for _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
        val = self.stack_out.pop()
        return val

    def peek(self) -> int:
        if len(self.stack_out) == 0:
            return self.stack_in[0]
        else:
            return self.stack_out[-1]

        

    def empty(self) -> bool:
        return len(self.stack_out) == 0 and  len(self.stack_in) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()