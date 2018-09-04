class Solution:
    # 方法1：利用默认参数求和
    def sumN1(self,i=[0],sum=[0]):
        i[0] +=1
        sum[0] += i[0]
        return sum[0]

    # 方法2：利用两个函数，
    # 一个函数充当递归函数的角色，另一个函数处理终止递归的情况。
    def sumN2(self,n):
        def sum0(n):
            return n
        
        def sumN(n):
            fun = {False:sum0,True:sumN}
            return n+fun[not not (n-1)](n-1)
        
        return sumN(n)

    # 方法3：利用and特性递归与终止函数，
    # and返回最右边为真的表达式或False，or返回最左边为真的表达式或False。
    def sumN3(self,n):
        def recursive(n):
            return n and recursive(n-1)+n
        
        return recursive(n)