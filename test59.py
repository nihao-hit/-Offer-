from collections import deque
class Solution:
    def getMaxOfWindows(self,array,n):
        '''
        :type array:list[int]
        :type n:int
        :rtype:list[int]
        '''
        if array is None or len(array) == 0 or n<=0 or n > len(array):
            return None
        tmp = deque()
        result = []
        for i in range(n):
            while len(tmp) != 0 and array[i] > array[tmp[-1]]:
                tmp.pop()
            tmp.append(i)
        for i in range(n,len(array)):
            result.append(array[tmp[0]])
            while len(tmp) != 0 and array[i] >= array[tmp[-1]]:
                tmp.pop()
            if len(tmp) != 0 and i-tmp[0]>=n:
                tmp.popleft()
            tmp.append(i)
        result.append(array[tmp[0]])
        return result