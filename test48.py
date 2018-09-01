class Solution():
    # 方法1：动态规划
    def getLongestSubstringWithoutDuplication1(self,string):
        '''
        :type string:str
        :rtype:int
        '''
        if string is None or len(string) == 0:
            return 0
        length = [0]*len(string)
        for i in range(len(string)):
            if i == 0:
                length[i] = 1
            else:
                dupIndex = string[i-length[i-1]:i].rfind(string[i])
                if dupIndex != -1:
                    length[i] = length[i-1]-dupIndex
                else:
                    length[i] = length[i - 1] + 1
        return length[-1]

    def getLongestSubstringWithoutDuplication2(self,string):
        if string is None or len(string) == 0:
            return 0
        indexs = {}
        i = curLen = 0
        maxLen = 0
        while i < len(string):
            try:
                index = indexs[string[i]][0]
                indexs[string[i]][0] = i
                curLen = min(i - index,curLen+1)
            except:
                indexs[string[i]] = [i]
                curLen += 1
            maxLen = max(maxLen,curLen)
            i += 1
        return maxLen