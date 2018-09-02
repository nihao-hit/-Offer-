from functools import reduce
class Solution:
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