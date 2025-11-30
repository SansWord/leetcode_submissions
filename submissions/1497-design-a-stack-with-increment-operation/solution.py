class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.data = []
        self.size = 0
        self.add = []
        

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.data.append(x)
            self.size += 1
            self.add.append(0)

    def pop(self) -> int:
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            adding = self.add.pop()
            res = self.data.pop() + adding
            if self.add:
                self.add[-1] += adding
            return res
        

    def increment(self, k: int, val: int) -> None:
        if self.size == 0:
            return

        if k <= self.size:
            self.add[k-1] += val
        else:
            self.add[-1] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
