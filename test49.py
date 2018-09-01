class Solution:
    def getUglyNumber(self,n):
        if n <= 0:
            return 0
        uglys = [1]*n
        index2 = 0
        index3 = 0
        index5 = 0
        for i in range(1,len(uglys)):
            uglys[i] = min([2*uglys[index2],3*uglys[index3],5*uglys[index5]])
            while 2*uglys[index2] <= uglys[i]:
                index2 += 1
            while 3*uglys[index3] <= uglys[i]:
                index3 += 1
            while 5*uglys[index5] <= uglys[i]:
                index5 += 1
        return uglys[-1]