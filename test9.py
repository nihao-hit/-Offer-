'''用两个栈实现队列'''
class Queue:
    def __init__(self):
        self._stack1 = []
        self._stack2 = []
    
    def appendTail(self,val):
        self._stack1.append(val)
    
    def deleteHead(self):
        if self._stack2:
            return self._stack2.pop()
        while self._stack1:
            self._stack2.append(self._stack1.pop())
        if self._stack2:
            return self._stack2.pop()
        else:
            raise ValueError('Empty Queue!')
    
    def __repr__(self):
        stack = []
        for i in range(len(self._stack2)-1,-1,-1):
            stack.append(self._stack2[i])
        for j in self._stack1:
            stack.append(j)
        return '<Queue of {}>'.format(stack)

'''用两个队列实现栈'''
class Stack:
    def __init__(self):
        self._queue1 = []
        self._queue2 = []
    
    def appendHead(self,val):
        if self._queue2:
            self._queue2.append(val)
        self._queue1.append(val)
    
    def deleteHead(self):
        if self._queue1:
            return self._queue1.pop()
        if self._queue2:
            return self._queue2.pop()
        else:
            raise ValueError('Empty Stack!')
    
    def __repr__(self):
        return '<Stack of {}>'.format(self._queue1 if self._queue1 else self._queue2)
s = Stack()