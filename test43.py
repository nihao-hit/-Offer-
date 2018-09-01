class Solution():
    # 方法1：遍历1-N的每个整数，求每位上1的个数
    def numberOf1Between1AndN1(self,n):
        '''
        :type n:int
        :rtype:int
        '''
        if n < 1:
            return 0
        count = 0
        for i in range(1,n+1):
            j = i
            while j>0:
                if j%10 == 1:
                    count += 1
                j //= 10
        return count
    
    # 方法2：
    def numberOf1Between1AndN2(self,n):
        chars = str(n)
        length = len(chars)
        count = int(chars[:length-1])
        if int(chars[length-1]) >= 1:
            count += 1
        if int(chars[0]) == 1:
            count += int(chars[1:])+1
        else:
            count += pow(10,length-1)
        for i in range(length-2,0,-1):
            prev = int(chars[:i])
            count += prev*pow(10,length-i-1)
            if int(chars[i]) == 1:
                after = int(chars[i+1:])
                count += after+1
            elif int(chars[i]) > 1:
                count += pow(10,length-i-1)
        return count