class MinStack:

    def __init__(self):
        self.stack = []
        self.supportingStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.supportingStack:
            self.supportingStack.append(val)
        elif self.supportingStack[-1] >= val:
            self.supportingStack.append(val)

    def pop(self) -> None:
        if self.supportingStack[-1] == self.stack[-1]:
            self.supportingStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.supportingStack[-1]