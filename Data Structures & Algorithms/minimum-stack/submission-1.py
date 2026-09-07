class MinStack:

    

    def __init__(self):
        self.stack = []
        self.min_value = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_value[-1] if self.min_value else val)
        self.min_value.append(val)        
    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min_value = self.min_value[:-1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]
        
        
