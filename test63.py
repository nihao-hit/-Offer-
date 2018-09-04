class Solution:
    def getMaxGain1(self,array):
        '''
        :type array:list[int]
        :rtype:int
        '''
        localMax = globalMax = 0 
        for i in range(1,len(array)):
            cur = array[i]-array[i-1]
            localMax = max(localMax+cur,cur)
            globalMax = max(globalMax,localMax)
        return globalMax

    def getMaxGain2(self,array):
        if not array or len(array)<2:
            return 0
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