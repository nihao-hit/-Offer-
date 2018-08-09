'''数组中重复的数字'''
class Solution:
    def findRepeatNum(self,nums,n):
        '''
        :type nums:List[int]
        :type n:int
        :rtype:int
        '''
        if len(nums) < 2 or n < 2:
            return None
        for i in range(len(nums)):
            if nums[i] < n:
                while nums[i] != i:
                    idx = nums[i]
                    if nums[idx] == idx:
                        return idx
                    else:
                        nums[i] = nums[idx]
                        nums[idx] = idx
            else:
                return None
'''
测试用例：
长度为n的数组中包含一个或多个重复的数字。
数组中不包含重复的数字。
无效输入测试用例（输入空指针；长度为n的数组中包含0-n-1之外的数字）。
'''

'''不修改数组找出重复的数字'''
def noAlterFindRepeatNum(nums,n):
    if len(nums) < 2 or n < 3:
        return None
    l,r = 1,n-1
    def countRange(nums,left,right):
        count = 0
        for i in nums:
            if i >= left and i <= right:
                count += 1
        return True if count > right-left+1 else False
    while l < r:
        mid = (l+r)//2
        if countRange(nums,l,mid):
            r = mid
        else:
            l = mid+1
    return mid