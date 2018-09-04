class Solution:
    def isContinuous(self,array):
        '''
        :type array:list[int]
        :rtype:bool
        '''
        if array is None or len(array) == 0:
            return False
        array.sort()
        numberGap = 0
        numberZero = len(list(filter(lambda x:x==0,array)))
        start = numberZero
        end = start+1
        while end<len(array):
            if array[start] == array[end]:
                return False
            numberGap += array[end]-array[start]-1
            start += 1
            end += 1
        if numberZero < numberGap:
            return False
        return True