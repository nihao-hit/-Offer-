'''矩阵中的路径'''
class Solution:
    def findPath(self,matrix,string):
        '''
        :type matrix:list[list[str]]
        :type string:str
        :rtype:bool
        '''
        if not matrix or not matrix[0] or not string:
            return False
        start = []
        rows,cols = len(matrix),len(matrix[0])
        for i in (0,rows-1):
            for j in range(cols):
                if matrix[i][j] == string[0]:
                    start.append((i,j))
        for j in (0,cols-1):
            for i in range(rows):
                if matrix[i][j] == string[0]:
                    start.append((i,j))
        if not start:
            return False
        path = [[0]*cols for i in range(rows)]
        def search(matrix,rows,cols,i,j,string,k,path):
            if k == len(string):
                return True
            hasPath = False
            if i >= 0 and i < rows and j >= 0 and j < cols and \
                matrix[i][j] == string[k] and path[i][j] == 0:
                path[i][j] = 1
                k += 1
                hasPath = search(matrix,rows,cols,i-1,j,string,k,path) \
                    or search(matrix,rows,cols,i,j+1,string,k,path) \
                    or search(matrix,rows,cols,i+1,j,string,k,path) \
                    or search(matrix,rows,cols,i,j-1,string,k,path)
                if not hasPath:
                    k -= 1
                    path[i][j] == 0
            return hasPath
        for index in start:
            if search(matrix,rows,cols,index[0],index[1],string,0,path):
                return True
        return False
'''
回溯法：通常在二维矩阵上找路径这类问题都可以应用回溯法解决。
递归难点:应用回溯法的递归不能通过函数参数返回结果，
因为不是单一递归栈，所以函数参数不能沿原路返回。
必须通过返回值返回结果。
'''