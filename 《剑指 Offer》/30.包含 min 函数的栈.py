"""
辅助栈
1. 使用一个辅助列表
2. 每次进行进栈操作，同时往辅助列表里压入当前最小元素
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.aux = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.aux:
            self.aux.append(x)
        else:
            m = self.aux[-1]
            if x > m:
                self.aux.append(m)
            else:
                self.aux.append(x)

    def pop(self) -> None:
        self.aux.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.aux[-1]
