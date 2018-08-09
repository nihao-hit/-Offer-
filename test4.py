'''
二维数组中的查找
'''
class Solution:
    def find(self,nums,target):
        '''
        :type nums:List[List[int]]
        :type target:int
        :rtype:bool
        '''
        rows,cols = len(nums),len(nums[0])
        if rows == 0:
            return False
        row,col = 0,cols-1
        while row < rows and col >= 0:
            if nums[row][col] == target:
                return True
            elif nums[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
'''
思路：在数组中选择一个数，根据它的大小判断要查找的数字可能出现的区域。
规律：应该选择行列两个方向一个递减一个递增的数字，如右上角，左下角。
    这样每次选择的数字唯一且每次判断可以剔除一行或一列。
'''