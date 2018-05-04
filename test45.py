'''
把数组排成最小的数
输入一个正整数数组，把数组里的所有数字拼接起来排成一个数，打印能拼接出的所有数字的最小的一个。
例如，输入数组{3，32，321}，打印321323。
'''
from functools import cmp_to_key


class test45():
    def PrintMinNumber(self,array):
        if array is None or len(array) == 0:
            return 0
        strArray = [str(i) for i in array]
        compare = lambda x,y:int(x+y)-int(y+x)
        strArray.sort(key=cmp_to_key(compare))
        return''.join(strArray)


t = test45()
arrays = [[1,2,3,4,5],[23,23,42,21],[2]]
for i in arrays:
    minNumber = t.PrintMinNumber(i)
    print(minNumber)