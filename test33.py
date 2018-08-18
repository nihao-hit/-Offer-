'''二叉搜索树的后序遍历序列'''
class BinaryTreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def verifyPostorderOfBST(self,nums):
        '''
        :type nums:list[int]
        :rtype:bool
        '''
        def recursive(nums,l,r):
            if l == r:
                return True
            k = l
            while k < r and nums[k] < nums[r]:
                k += 1
            if k < r:
                for i in range(k,r):
                    if nums[i] < nums[r]:
                        return False
                return recursive(nums,l,k-1) and recursive(nums,k,r-1)
            return recursive(nums,l,r-1)
        return recursive(nums,0,len(nums)-1)