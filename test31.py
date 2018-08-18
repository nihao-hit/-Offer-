'''栈的压入、弹出序列'''
class Solution:
    def isPopOrder(self,pPush,pPop):
        '''
        :type pPush:list[int]
        :type pPop:list[int]
        :rtype:bool
        '''
        stack = []
        i = 0
        for j in pPop:
            while not stack or i < len(pPush) and stack[-1] != j:
                stack.append(pPush[i])
                i += 1
            if not stack or stack.pop() != j:
                return False
        return True