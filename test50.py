class Solution:
    def getFirstNotRepeatingStr(self,string):
        if string is None or len(string) == 0:
            return None
        value = {}
        n = len(string)
        index = n
        for i in range(n):
            value.setdefault(string[i],[]).append(i)
        for i in value.values():
            if len(i) == 1 and i[0] < index:
                index = i[0]
        return string[index] if index < n else None
    
# 题目2：字符流中第一个只出现一次的字符
class CharStatistics:
    def __init__(self,val):
        self.string = val
        self.index = 0
        self.indexs = {}
        self.charIdx = 0

    def read(self):
        try:
            temp = self.indexs[self.string[self.index]]
            temp.append(self.index)
            self.string[temp[-1]] = self.string[temp[-2]] = '$'
        except:
            self.indexs[self.string[self.index]] = [self.index]
        finally:
            self.index += 1
            while self.charIdx < self.index and self.string[self.charIdx] == '$':
                self.charIdx += 1
        return self.string[self.charIdx] if self.charIdx < self.index else None