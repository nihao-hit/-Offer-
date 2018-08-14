'''机器人的运动范围'''
class Solution:
    def numOfCell(self,rows,cols,k):
        '''
        :type matrix:list[list[int]]
        :type k:int
        :rtype:int
        '''
        if rows <= 0 or cols <= 0 or k < 0:
            return 0
        path = [[0]*cols for i in range(rows)]
        def search(rows,cols,i,j,k,path):
            if i < 0 or j < 0 or i >= rows or j >= cols or path[i][j]:
                return 0
            num = 0
            for val in str(i)+str(j):
                num += int(val)
            if num > k:
                return 0
            path[i][j] = 1
            return 1+search(rows,cols,i-1,j,k,path)+search(rows,cols,i,j+1,k,path) \
                   +search(rows,cols,i+1,j,k,path)+search(rows,cols,i,j-1,k,path)
        return search(rows,cols,0,0,k,path)