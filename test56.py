from functools import reduce
class Solution:
    # 小技巧：两个不同数异或结果一定不为0，按异或结果为一第一位划分数组。
    def findNumAppearOnce(self,nums):
        '''
        :type nums:list[int]
        :rtype:tuple
        '''
        def yihuo(a,b):
            return a^b
        
        def findBinaryFirst1(num):
            i = 1
            while num > 0:
                if num & 1 == 1:
                    return i
                i+= 1
                num = num >> 1
            return -1

        def isOne(num,idx):
            return num >> (idx-1) & 1

        pivot = reduce(yihuo,nums)
        idx = findBinaryFirst1(pivot)
        nums1,nums2 = [],[]
        for num in nums:
            if isOne(num,idx):
                nums1.append(num)
            else:
                nums2.append(num)
        return reduce(yihuo,nums1),reduce(yihuo,nums2)
    
    # 题目2：数组中唯一只出现一次的数字（其他数字出现三次）
    def findNumAppearOnce3(self,nums):
        def bitPartition(num,bits):
            i = 0
            while num > 0:
                bits[i] += num & 1
                num = num >> 1
                i += 1

        bits = [0]*32
        for num in nums:
            bitPartition(num,bits)
        result = 0
        for i in range(31,-1,-1):
            result += bits[i]%3*pow(2,i)
        return result