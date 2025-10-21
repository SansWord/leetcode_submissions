class MyStack:

    def __init__(self):
        self.firstQ = deque()
        self.secondQ = deque()
        self.atFirst = True

    def push(self, x: int) -> None:
        main, secondary = self.getData()

        while len(secondary) != 0:
            main.append(secondary.pop())
        secondary.append(x)
        

    def pop(self) -> int:
        main, secondary = self.getData()
        result = secondary.popleft()
        self.atFirst = not self.atFirst
        return result
        

    def top(self) -> int:
        main, secondary = self.getData()
        return secondary[0]
        

    def empty(self) -> bool:
        return len(self.firstQ) + len(self.secondQ) == 0

    def getData(self) -> tuple[deque[int], deque[int]]:
        if self.atFirst:
            main, secondary = self.firstQ, self.secondQ
        else:
            main, secondary = self.secondQ, self.firstQ
        while len(secondary) > 1:
            main.append(secondary.popleft())
        
        if len(secondary) == 0 and len(main) != 0:
            secondary.append(main.popleft())

        return main, secondary


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()