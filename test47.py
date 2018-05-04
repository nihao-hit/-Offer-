'''
礼物的最大价值
在一个mXn的棋盘的每一个都放有一个礼物，每个礼物都有一定的价值（大于0）。
你可以从棋盘的左上角开始拿礼物，每次向下或向右移动一步，直到右下角。
给定一个棋盘及上面的礼物，请计算你最多能拿多少价值的礼物。
'''
from functools import reduce
class test47():
    def getMaxValue(self,gift):
        if gift is None or len(gift) == 0:
            return 0
        elif len(gift) == 1:
            return reduce(lambda x,y:x+y,gift[0])
        elif len(gift[0]) == 1:
            value = 0
            for row in gift:
                value += row[0]
            return value
        '''
        for row in gift:
            for col in row:
                if col <= 0:
                    return 0
        '''
        row = len(gift)
        col = len(gift[0])
        value = [[0]*col for i in range(row)]
        for row in range(len(gift)):
            for col in range(len(gift[0])):
                if row == 0 and col == 0:
                    value[row][col] = gift[row][col]
                elif row == 0:
                    value[row][col] = value[row][col-1] + gift[row][col]
                elif col == 0:
                    value[row][col] = value[row-1][col] + gift[row][col]
                else:
                    value[row][col] = max(value[row-1][col],value[row][col-1]) + gift[row][col]
        return value[-1][-1]


t = test47()
ns = [[[1,2,3,4],[2,2,3,4],[3,2,3,4],[4,2,3,4]],[[1,2,3,4]],[[1],[2],[3],[4]],[]]
for n in ns:
    maxValue = t.getMaxValue(n)
    print(maxValue)
