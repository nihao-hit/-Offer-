'''
把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为26个英文字母，0-a，25-z。
一个数字可能有多个翻译。
例如，12258有5种不同的翻译。分别是bccfi，bwfi，bczi，mcfi，mzi。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方案。
'''
class test46():
    def GetTranslationCount(self,n):
        if n < 0:
            return 0
        strN = str(n)
        counts = [0]*len(strN)
        num = len(strN)-1
        i = num
        while(i >= 0):
            if i == num:
                counts[i] = 1
            elif i == num-1:
                if int(strN[i:]) >= 10 and int(strN[i:]) <= 25:
                    counts[i] = 2
                else:
                    counts[i] = 1
            else:
                if int(strN[i:i+2]) >= 10 and int(strN[i:i+2]) <= 25:
                    counts[i] = counts[i+1]+counts[i+2]
                else:
                    counts[i] = counts[i+1]
            i -= 1
        return counts[0]


ns = [1,22,34224532,-1,0,25,26]
t = test46()
for i in ns:
    count = t.GetTranslationCount(i)
    print(count)
