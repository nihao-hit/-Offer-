'''顺时针打印矩阵'''
class Solution:
    def clockwisePrintMatrix(self,nums):
        '''
        :type nums:list[list[int]]
        :rtype:void
        '''
        lrow,rrow,lcol,rcol = 0,len(nums)-1,0,len(nums[0])-1
        while lrow <= rrow and lcol <= rcol:
            for i in range(lcol,rcol+1):
                print(nums[lcol][i])
            if rrow > lrow:
                for j in range(lrow+1,rrow+1):
                    print(nums[j][rcol])
                if rcol > lcol:
                    for k in range(rcol-1,lcol-1,-1):
                        print(nums[rrow][k])
                if rrow > lrow+1:    
                    for v in range(rrow-1,lrow,-1):
                        print(nums[v][lcol])
            lrow,rrow,lcol,rcol = lrow+1,rrow-1,lcol+1,rcol-1
'''
分解问题为两个子问题：一是将矩阵分为若干个圈，二是顺时针打印每个圈。
犯错：1：对于顺时针打印每个圈的规律没有分析清楚；
      2：使用了while而不是for循环，导致循环开始条件和结束条件不确定。
'''