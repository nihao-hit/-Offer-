'''
求1+2+···+n
求1+2+···+n，要求不能使用乘除法，if，while，for，else，switch，case等关键字及条件判断语句(A?B:C)
'''
class test64():
    def Sum_Solution(self,n):
        return self.sumN(n)
    def sum0(self,n):
        return n
    def sumN(self,n):
        fun = {False:self.sum0,True:self.sumN}
        return n+fun[not not n](n-1)
    def Sum_Solution2(self,n):
        return n and self.Sum_Solution(n-1)+n
t = test64()
print(t.Sum_Solution2(5))