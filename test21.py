'''调整数组顺序使奇数位于偶数前面'''
class Solution:
    @classmethod
    def isEven(cls,num):
        '''
        :type num:int
        :rtype:bool
        '''
        return num%2 == 0

    def oddEven(self,nums,fn):
        '''
        :type nums:list[int]
        :rtype:list[int]
        '''
        def swap(nums,l,r):
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
        
        length = len(nums)
        l,r = 0,length-1
        while l < r:
            while l < r and not fn(nums[l]):
                l += 1
            while l < r and fn(nums[r]):
                r -= 1
            if l < r:
                swap(nums,l,r)
        return nums