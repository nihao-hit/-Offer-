'''重建二叉树'''
class BinaryTreeNode:
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None


class Solution:
    def rebuildBinaryTree(self,prevorder,inorder):
        '''
        :type prevorder:List[int]
        :type inorder:List[int]
        :rtype:ListNode
        '''
        def recursion(prevorder,pS,pE,inorder,iS,iE):
            val = prevorder[pS]
            key = inorder.index(val)
            leftNum = key-iS
            rightNum = iE-key
            head = BinaryTreeNode(val)
            if leftNum > 0:
                head.left = recursion(prevorder,pS+1,pS+leftNum,inorder,iS,key-1)
            else:
                head.left = None
            if rightNum > 0:
                head.right = recursion(prevorder,pS+leftNum+1,pE,inorder,key+1,iE)
            else:
                head.right =  None
            return head
        return recursion(prevorder,0,len(prevorder)-1,inorder,0,len(inorder)-1)