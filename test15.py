'''二进制中1的个数'''
class Solution:
    # 方法1：把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0。
    # 那么一个整数的二进制表示中有多少个1，就可以进行多少次这样的操作。
    def countOfBinary1(self,n):
        '''
        :type n:int
        :rtype:int
        '''
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n-1) & n
        return count
    
    # 方法2
    def countOfBinary2(self,n):
        '''
        :type n:int
        :rtype:int
        '''
        if n < 0:
            n = bin(n & 0xffffffff)
        else:
            n = bin(n)
        return n.count('1')
    
    # 用一条语句判断一个整数是不是2的整数次方
    def powerOfTwo(self,n):
        '''
        :type n:int
        :rtype:bool
        '''
        return True if n & (n-1) == 0 else False
    
    # 输入两个整数m和n，计算需要改变m的二进制表示中多少位才能得到n。
    def countOfDiff(self,m,n):
        '''
        :type m:int
        :type n:int
        :rtype:int
        '''
        return bin(m ^ n).count('1')