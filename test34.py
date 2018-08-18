'''二叉树中和为某一值的路径'''
import copy
class BinaryTreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def pathOfSum(self,root,num):
        '''
        :type root:BinaryTreeNode
        :rtype:list[list[int]]
        '''
        result = []
        def recursive(node,num,temp,path,result):
            if node:
                temp += node.val
                path.append(node.val)
                if not node.left and not node.right:
                    if temp == num:
                        result.append(path)
                else:
                    if temp < num:
                        recursive(node.left,num,temp,copy.copy(path),result)
                        recursive(node.right,num,temp,copy.copy(path),result)
        recursive(root,num,0,[],result)
        return result