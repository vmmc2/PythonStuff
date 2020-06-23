class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.size = 0
        # primeiro elemento da tupla eh o proprio elemento em si.
        # segundo elemento da tupla eh o elemento minimo da stack ate aquela altura.

    def push(self, x: int) -> None:
        if self.size == 0:
            self.s.append((x, x))
            self.size += 1
        else:
            self.s.append((x, min(x, self.s[-1][1])))
            self.size += 1
        return

    def pop(self) -> None:
        self.s.pop()
        self.size -= 1
        return 
        
    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
