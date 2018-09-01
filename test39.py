class Solution:
    # 方法一：根据partition函数找中位数
    def moreThanHalfOfNum1(self,nums):
        '''
        :type nums:list[int]
        :rtype:int
        '''
        n = len(nums)
        def getPivot(nums,i,j):
            while i < j:
                if nums[i] != nums[i+1]:
                    return max(nums[i],nums[i+1])
                i += 1
            return -1
        
        def partition(nums,i,j,num):
            while i < j:
                while i < j and nums[i] < num:
                    i += 1
                while i < j and nums[j] >= num:
                    j -= 1
                if i < j:
                    nums[i],nums[j] = nums[j],nums[i]
            return i

        def recursive(num,i,j,k):
            num = getPivot(nums,i,j)
            if i == j or num == -1:
                return nums[i]
            else:
                index = partition(nums,i,j,num) 
                if k == index:
                    return nums[k]
                elif k > index:
                    return recursive(nums,index+1,j,k)
                else:
                    return recursive(nums,i,index-1,k)
        
        return recursive(nums,0,len(nums)-1,(len(nums)-1)>>2)
    
    def moreThanHalfOfNum2(self,nums):
        curNum = curCount = 0
        for i in nums:
            if i == curNum:
                curCount += 1
            elif curCount > 0:
                curCount -= 1
            else:
                curNum = i
        return curNum