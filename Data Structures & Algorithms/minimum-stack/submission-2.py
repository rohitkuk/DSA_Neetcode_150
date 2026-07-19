class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = 1000
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.update_min(self.top())

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.update_min(self.top())
        
    def top(self) -> int:
        return self.stack[-1]
        
    def update_min(self,val):
        self.min_ =  min(self.min_, val)

    def getMin(self) -> int:
        return min(self.stack)
        
