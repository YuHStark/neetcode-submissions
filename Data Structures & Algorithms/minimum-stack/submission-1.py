class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.ministack:
            self.ministack.append(val)
        else:
            self.ministack.append(min(val,self.ministack[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.ministack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ministack[-1]
        
