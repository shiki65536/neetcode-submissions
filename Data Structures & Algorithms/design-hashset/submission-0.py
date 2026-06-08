class MyHashSet:

    def __init__(self):
        self.stack = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.stack.append(key)
        

    def remove(self, key: int) -> None:
         if self.contains(key):
            self.stack.remove(key)       

    def contains(self, key: int) -> bool:
        if len(self.stack) == 0:
            return False
        if key in self.stack:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)