class Solution:
    # 方法1：循环
    def getTranslationCount1(self,n):
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

    # 方法2：递归
    def getTranslationCount2(self,n):
        def recursive(string,length,i):
            if i == length:
                return 1
            if i+1 < length and 9 < int(string[i:i+2]) < 26:
                return recursive(string,length,i+2)+ \
                       recursive(string,length,i+1)
            else:
                return recursive(string,length,i+1)
        
        string = str(n)
        return recursive(string,len(string),0)