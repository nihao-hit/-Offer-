class Solution:
    def multiply(self,A):
        '''
        :type A:list[int]
        :rtype:list[int]
        '''
        n = len(A)
        preMultiply,backMultiply,result = [[1]*n for i in range(3)]
        preMultiply[0],backMultiply[-1] = A[0],A[-1]
        for i in range(1,n):
            preMultiply[i] = preMultiply[i-1]*A[i]
        for i in range(n-2,-1,-1):
            backMultiply[i] = backMultiply[i+1]*A[i]
        
        result[0],result[-1] = backMultiply[1],preMultiply[-2]
        for i in range(1,n-1):
            result[i] = preMultiply[i-1]*backMultiply[i+1]
        return result