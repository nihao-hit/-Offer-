'''
1~n整数中1出现的次数
输入一个整数n，求1~n这n个整数的十进制表示中1出现的次数。
例如，输入12，1~12中出现了1，10，11，12，1一共出现了5次。
'''
class test43():
    def NumberOf1Between1AndN(self,n):
        if n < 1:
            return 0
        global count
        count = 0
        for i in range(1,n+1):
            j = i
            while j>0:
                if j%10 == 1:
                    count += 1
                j //= 10
        return count


t = test43()
nList = [5,10,55,99,0,1,10000]
for i in nList:
    count = t.NumberOf1Between1AndN(i)
    print(count)