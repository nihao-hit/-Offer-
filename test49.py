'''
丑数
我们把只包含2，3，5的因子的数叫做丑数。
求按从小到大的顺序的第1500个丑数。
例如：6，8都是丑数，但14不是，因为它包含7。
习惯上我们把1当作第一个丑数。
'''
class test49():
    def getUglyNumber(self,n):
        if n <= 0:
            return 0
        i = 0
        count = 0
        while(count < n):
            i += 1
            j = i
            while(j%2 == 0):
                j /= 2
            while(j%3 == 0):
                j /= 3
            while(j%5 == 0):
                j /= 5
            if j == 1:
                count += 1
        return i
    def betterGetUglyNumber(self,n):
        if n <= 0:
            return 0
        uglys = [1]*n
        index2 = 0
        index3 = 0
        index5 = 0
        for i in range(1,len(uglys)):
            uglys[i] = min([2*uglys[index2],3*uglys[index3],5*uglys[index5]])
            while 2*uglys[index2] <= uglys[i]:
                index2 += 1
            while 3*uglys[index3] <= uglys[i]:
                index3 += 1
            while 5*uglys[index5] <= uglys[i]:
                index5 += 1
        return uglys[-1]


t = test49()
ns = [2,3,4,5,6,1,0,1500]
for i in ns:
    maxUgly = t.getUglyNumber(i)
    print(maxUgly)
    maxUgly = t.betterGetUglyNumber(i)
    print(maxUgly)