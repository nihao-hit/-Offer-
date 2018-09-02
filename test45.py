from functools import cmp_to_key
class Solution:
    # 方法1：快排
    def printMinNumber1(self,array):
        strArray = [str(i) for i in array]
        compare = lambda x,y:int(x+y)-int(y+x)
        strArray.sort(key=cmp_to_key(compare))
        return ''.join(strArray)

    # 方法2：插入排序
    def printMinNumber2(self,nums):
        '''
        :type nums:list[int]
        :rtype:int
        '''
        nums = [str(i) for i in nums]
        for i in range(1,len(nums)):
            j = i
            while j > 0:
                if int(nums[j]+nums[j-1]) < int(nums[j-1]+nums[j]):
                    nums[j],nums[j-1] = nums[j-1],nums[j]
                j -= 1
        return ''.join(nums) 