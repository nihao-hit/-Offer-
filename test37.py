'''序列化二叉树'''
class BinaryTreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def serialize(self,root):
        '''
        :type root:BinaryTreeNode
        :rtype:list
        '''
        result = []
        def recursive(node,result):
            if node:
                result.append(node.val)
                recursive(node.left,result)
                recursive(node.right,result)
            else:
                result.append('$')
        recursive(root,result)
        return result
    
    def deserialize(self,nums):
        '''
        :type nums:list
        :rtype:BinaryTreeNode
        '''
        def recursive(nums,length,index):
            if index < length and nums[index] != '$':
                root = BinaryTreeNode(nums[index])
                root.left,index = recursive(nums,length,index+1)
                root.right,index = recursive(nums,length,index+1)
                return root,index
            return None,index
        return recursive(nums,len(nums)-1,0)[0]