'''打印从1到最大的n位数'''
from itertools import zip_longest
class Solution:
    # 方法一：考虑到大数问题，在字符串上模拟数字加法的解法
    def print1ToN1(self,n):
        '''
        :type n:int
        :rtype:void
        '''
        if n <= 0:
            return

        def printResult(num):
            head0 = True
            for i in num:
                if head0 and i != '0':
                    head0 = False
                if not head0:
                    print(i,end='')
            print()
                    
        integers = {i:'{}'.format(i) for i in range(10)}
        chars = {'{}'.format(i):i for i in range(10)}
        result = ['0']*(n+1)
        while result[0] == '0':
            for i in range(1,11):
                if i == 10:
                    index = n
                    while index > 0 and result[index] == '9':
                        result[index] = integers[0]
                        index -= 1
                    result[index] = integers[chars[result[index]]+1]
                else:
                    result[n] = integers[i]
                if result[0] == '1':
                    break
                printResult(result)
    
    # 方法二：把问题转换为数字排列的解法，用递归实现全排列
    def print1ToN2(self,n):
        if n <= 0:
            return 
        
        def printResult(num):
            head0 = True
            for i in num:
                if head0 and i != '0':
                    head0 = False
                if not head0:
                    print(i,end='')
            print()

        def recursive(nums,integers,n,index):
            if index == n+1:
                printResult(nums)
                return
            for i in range(10):
                nums[index] = integers[i]
                recursive(nums,integers,n,index+1)

        integers = {i:'{}'.format(i) for i in range(10)}
        result = [integers[0]]*(n+1)
        recursive(result,integers,n,1)

    # 求任意两个整数的加法
    def getSumOfTwoIntegers(self,num1,num2):
        '''
        :type num1:int
        :type num2:int
        :rtype:void
        '''
        def printResult(num,signal):
            if signal == -1:
                print('-',end='')
            head0 = True
            for i in range(len(num)-1,-1,-1):
                if head0 and num[i] != '0':
                    head0 = False
                if not head0:
                    print(num[i],end='')
            print()

        chars = {i:'{}'.format(i) for i in range(10)}
        integers = {'{}'.format(i):i for i in range(10)}
        str12 = list(zip_longest(reversed(str(abs(num1))),reversed(str(abs(num2))),fillvalue='0'))
        length = len(str12)
        result = []
        signal = 1
        if num1 >= 0 and num2 >= 0 or num1 < 0 and num2 < 0:
            if num1 < 0:
                signal = -1
            i,carry = 0,0
            while i < length:
                temp = integers[str12[i][0]]+integers[str12[i][1]]
                carry,add = divmod(temp+carry,10)
                result.append(chars[add])
                i += 1
            if carry > 0:
                result.append(chars[carry])
        else:
            if num1+num2 < 0:
                signal = -1
            if abs(num1) > abs(num2):
                flag = 0
            else:
                flag = 1
            i,borrow = 0,0
            while i < length:
                if integers[str12[i][flag]] >= integers[str12[i][1-flag]]+borrow:
                    result.append(chars[integers[str12[i][flag]]-integers[str12[i][1-flag]]-borrow])
                    borrow = 0
                else:
                    result.append(chars[10+integers[str12[i][flag]]-integers[str12[i][1-flag]]-borrow])
                    borrow = 1
                i += 1
        printResult(result,signal)             