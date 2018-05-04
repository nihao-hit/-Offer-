'''
连续子数组的最大和
输入一个整型数组，数组里有正数也有负数，数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。要求时间复杂度为O(n).
'''
'''
BUG:当输入数组全是负数时，普通方法sum为0，DPsum为最大的负数。
'''
class test42():
    def FindGreatestSumOfSubArray(self,array):
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

    def DP(self,array):
        if array is None or len(array) == 0:
            return -1
        sumArray = [0]*len(array)
        for i in range(len(array)):
            if i == 0 or sumArray[i-1] <= 0:
                sumArray[i] = array[i]
            else:
                sumArray[i] = sumArray[i-1] + array[i]
        return max(sumArray)



array1 = [1,-2,3,10,-4,7,2,-5]
array2 = [1,2,3,4,5,6,7,8,9]
array3 = [-i for i in array2]
array4 = []
t = test42()
sum1 = t.FindGreatestSumOfSubArray(array1)
sum2 = t.FindGreatestSumOfSubArray(array2)
sum3 = t.FindGreatestSumOfSubArray(array3)
sum4 = t.FindGreatestSumOfSubArray(array4)
print(sum1,sum2,sum3,sum4)
sum5 = t.DP(array1)
sum6 = t.DP(array2)
sum7 = t.DP(array3)
sum8 = t.DP(array4)
print(sum5,sum6,sum7,sum8)
