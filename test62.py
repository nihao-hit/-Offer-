'''
圆圈中最后剩下的数字
0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次删除第m个数字，然后移动到第m+1个数字。
求这个圆圈最后剩下的数字。
公式：第一个被删除的数字k=(m-1)%n
        f(n,m)={0              n=1
               {[f(n-1,m)+m]%n n>1
'''
class test62():
    def LastRemaining(self,array,m):
        if array is None or len(array) == 0 or m <= 0:
            return -1

        def outOfIndex():
            nonlocal index
            if index >= len(array):
                index = 0
        index = 0
        while len(array)>1:
            for i in range(m-1):
                outOfIndex()
                index += 1
            outOfIndex()
            array.pop(index)
            outOfIndex()
        return array[0]
    def equation(self,n,m):
        if n<1 or m<1:
            return -1
        lastNumber = 0
        for i in range(2,n+1):
            lastNumber = (lastNumber+m)%i
        return lastNumber
t = test62()
arrayS = [[0,1,2,3,4],[0,1,2,3,4,5]]
mS  = [3,7]
for i in range(len(arrayS)):
    lastNumber = t.LastRemaining(arrayS[i],mS[i])
    print(lastNumber)
lastNumber = t.equation(5,3)
print(lastNumber)
