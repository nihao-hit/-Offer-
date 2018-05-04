'''
和为s的两个数字
输入一个递增序列和一个数字s，输入和为s的两个数。如果有多对数和为s，则输出任意一对即可。
'''
class test57():
    def findNumbersWithSum(self,array,s):
        if array is None or len(array) == 0:
            return None,None
        start = 0
        end = len(array)-1
        while(start < end):
            if array[start]+array[end] == s:
                return array[start],array[end]
            elif array[start]+array[end] < s:
                start += 1
            else:
                end -= 1

t = test57()
arrayS = [[-2,-1,0,1,2],[0,0,0,0],None,[]]
sS = [3,0,3,3]
for i in range(len(sS)):
    num1,num2 = t.findNumbersWithSum(arrayS[i],sS[i])
    print('({},{})'.format(num1,num2))


'''
和为s的连续正数序列
输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
例如：输入15，由于1+2+3+4+5=4+5+6=7+8，所以打印（1~5），（4~6），（7，8）。
'''
from functools import reduce
class test572():
    def findContinuousSequence(self,s):
        if s is None or s <= 0:
            return None
        result = []
        start = 1
        end = 2
        he = start + end
        while start <= s//2 and start < end:
            if he == s:
                result.append([i for i in range(start,end+1)])
                end += 1
                he += end
            elif he < s:
                end += 1
                he += end
            else:
                he -= start
                start += 1
        return result
t = test572()
sS = [15,4,0,None]
for i in sS:
    sequence = t.findContinuousSequence(i)
    print(sequence)