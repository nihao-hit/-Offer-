'''包含min函数的栈'''
class Stack:
    def __init__(self):
        self.storage = []
        self.minS = []
    
    def push(self,val):
        if not self.minS or self.minS and val <= self.minS[-1]:
            self.minS.append(val)
        self.storage.append(val)
    
    def pop(self):
        if self.storage:
            if self.storage[-1] == self.minS[-1]:
                self.minS.pop()
            return self.storage.pop()
        else:
            raise ValueError('Empty Stack!')
    
    def min(self):
        if self.minS:
            return self.minS[-1]
        else:
            raise ValueError('Empty Stack!')
    
    def __repr__(self):
        return '<Stack {}>'.format(self.storage)
'''
把每次的最小元素（之前的最小元素与新压入栈的元素两者的较小值）保存在辅助栈。
'''