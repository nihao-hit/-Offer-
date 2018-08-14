'''剪绳子'''
class Solution:
    # 方法一：DP，定义函数f(n)是把长度为n的绳子剪成若干段后各段长度乘积的最大值。
    # 在剪第一刀的时候，我们有n-1种剪法。f(n) = max(f(i)*f(n-i))，得到递归公式。
    # 难点：n=2，n=3都是特例。f(2)!=1,f(3)!=2，
    # 当f(2),f(3)作为子问题在递归公式右边的时候，可以选择不剪，以长度作为f(n)值。
    def cutRope1(self,n):
        '''
        :type n:int
        :rtype:int
        '''
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        result = [0]*(n+1)
        result[1],result[2],result[3] = 1,2,3
        for i in range(4,n+1):
            maxVal = i
            for j in range(1,(i+2)//2):
                temp = result[j]*result[i-j]
                if temp > maxVal:
                    maxVal = temp
            result[i] = maxVal
        return result[-1]
    
    # 方法2：贪婪算法，当n>=5时，尽可能多的剪长度为3的绳子；当剩下的绳子长度为4时，剪成2，2。
    def cutRope2(self,n):
        '''
        :type n:int
        :rtype:int
        '''
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        result = 1
        while n >= 5:
            n -= 3
            result *= 3
        return result*n