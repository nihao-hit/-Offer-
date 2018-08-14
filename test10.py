'''斐波那契数列'''
class Solution:
    def fibonacci1(self,n):
        '''
        :type n:int
        :rtype:int
        '''
        def recursion(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            return recursion(n-1)+recursion(n-2)
        return recursion(n) 
    
    def fibonacci2(self,n):
        '''
        :type n:int
        :rtype:int
        '''
        a,b = 0,1
        for i in range(n):
            a,b = b,a+b
        return a