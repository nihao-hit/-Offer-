class Solution:
    def findGreatestSumOfSubArray(self,array):
        if array is None or len(array) == 0:
            return -1
        curSum = 0
        maxSum = 0
        for i in array:
            if i > i+curSum:
                curSum = i
            else:
                curSum += i
                if curSum > maxSum:
                    maxSum = curSum
        return maxSum