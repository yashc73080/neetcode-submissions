class MinStack:

    def __init__(self):
        self.stack = []

        # Separate stack to track min through each step
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if len(self.min_stack) == 0:
            self.min_stack.append(value)
        else:
            to_add = min(value, self.min_stack[-1])
            self.min_stack.append(to_add)

    def pop(self) -> None:
        self.stack.pop()

        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
