class BinaryTreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def KthNode(self,root,k):
        '''
        :type root:BinaryTreeNode
        :type k:int
        :rtype:BinaryTreeNode
        '''
        def recursive(node,k,result):
            if node:
                recursive(node.left,k,result)
                k[0] -= 1
                if k[0] <= 0:
                    if k[0] == 0:
                        result.append(node)
                    return
                recursive(node.right,k,result)
        
        result = []
        recursive(root,[k],result)
        return result[0]