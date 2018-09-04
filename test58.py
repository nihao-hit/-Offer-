class Solution:
    def reverseStr(self,mStr):
        '''
        :type mStr:str
        :rtype:str
        '''
        def reverseWord(array,start, end):
            while start < end:
                array[start],array[end] = array[end],array[start]
                start += 1
                end -= 1
        
        if len(mStr) == 0:
            return ''
        array = list(mStr)
        start = end = 0
        while end < len(mStr) and start < len(mStr):
            while end < len(mStr) and mStr[end] != ' ':
                end += 1
            end -= 1
            reverseWord(array,start,end)
            end += 2
            start = end
        reverseWord(array,0,len(array)-1)
        return ''.join(array)

    # 题目2：左旋转字符串
    def leftSpinStr(self,mStr,n):
        def reverseWord(array,start, end):
            while start < end:
                array[start],array[end] = array[end],array[start]
                start += 1
                end -= 1
        
        if len(mStr) == 0 or n<0 or n > len(mStr):
            return ''
        if n == 0:
            return mStr
        array = list(mStr)
        reverseWord(array,0,n-1)
        reverseWord(array,n,len(mStr)-1)
        reverseWord(array,0,len(mStr)-1)
        return ''.join(array)