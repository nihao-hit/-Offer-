'''
扑克牌中的顺子
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这五张牌是否连续。
2-10为数字本身，A为1，J为11，Q为12，K为13。大小王可以看成任意数字。
'''
class  test61():
    def isContinuous(self,array):
        if array is None or len(array) == 0:
            return False
        array.sort()
        numberZero = 0
        numberGap = 0
        numberZero = len(list(filter(lambda x:x==0,array)))
        start = numberZero
        end = start+1
        while end<len(array):
            if array[start] == array[end]:
                return False
            numberGap += array[end]-array[start]-1
            start += 1
            end += 1
        if numberZero < numberGap:
            return False
        return True
t = test61()
array = [[2,4,8,5,6],[2,4,5,6,0],[2,4,4,5,6],[2,5,6,0,0]]
for i in array:
    flag = t.isContinuous(i)
    print(flag)