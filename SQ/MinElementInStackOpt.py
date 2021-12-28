class MinStack:

    def __init__(self):
        self.stack = []
        self.minElement = float("-inf")
        self.n = 0

    def push(self, val: int) -> None:
        if self.n == 0:
            self.minElement = val
            self.n+=1
            self.stack.append(val)
            return

        if val < self.minElement:
            self.stack.append(2*val - self.minElement)
            self.minElement = val
        else:
            self.stack.append(val)
        self.n +=1
    def pop(self) -> None:

        if self.n == 1:
            self.minElement = float("inf")
            val = self.stack.pop()
            self.n-=1
            return val

        elif self.stack[-1] < self.minElement:
            val = self.minElement
            self.minElement = 2*self.minElement - self.stack[-1]
            self.stack.pop()
            self.n-=1
            return val
        else:
            self.n-=1
            return self.stack.pop()

    def top(self) -> int:
        if self.stack[-1] <= self.minElement:
            return self.minElement
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minElement

