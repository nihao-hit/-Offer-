'''旋转数组的最小数字'''
class Solution:
    def minOfRotateList(self,nums):
        '''
        :type nums:List[int]
        :rtype:int
        '''
        if not nums:
            return None
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r)//2
            while nums[l] == nums[mid] and l < mid:
                l += 1
            while nums[r] == nums[mid] and mid < r:
                r -= 1
            if mid-1 >= 0:
                if nums[mid-1] > nums[mid]:
                    return nums[mid]
                else:
                    if nums[mid] > nums[r]:
                        l = mid+1
                    else:
                        r = mid-1        
            else:
                return nums[mid]
        return nums[0]
'''
规律：最小的数有三种情况：1：小于左邻。2：没有左邻，在数组最左边。
'''