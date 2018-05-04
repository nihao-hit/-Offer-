'''
股票的最大利润
假设把某股票的价格按照时间顺序存储在数组中，求一次买卖股票能得到的最大收益。
例如：[9,11,8,5,7,12,16,14]。如果我们在5买入，16卖出，得到最大收益为11.
'''
class test63():
    def getMaxGain(self,array):
        if not array or len(array)<2:
            return None
        minIn = array[0]
        maxOut = array[1]
        maxGain = maxOut-minIn
        for i in range(2,len(array)):
            if array[i-1]<minIn:
                minIn = array[i-1]
            maxOut = array[i]
            if maxOut - minIn > maxGain:
                maxGain = maxOut - minIn
        return maxGain
t = test63()
arrayS = [[9,11,8,5,7,12,16,14],[1,2],[6,5,4,3,2,1]]
for array in arrayS:
    maxGain = t.getMaxGain(array)
    print(maxGain)