class BinaryTreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # 方法1：递归树下行时，当前深度作为参数向下传递，
    # 递归树上行时，最大深度作为返回值向上传递。
    def getDepth1(self,root):
        '''
        :type root:BinaryTreeNode
        :rtype:int
        '''
        def recursive(node,depth=0):
            if node:
                depth += 1
                if not node.left and not node.right:
                    return depth
                return max(recursive(node.left,depth),
                           recursive(node.right,depth))
            return depth
        
        return recursive(root)
    
    # 方法2：计算递归树最大深度
    def getDepth2(self,root):
        def recursive(node):
            if node:
                return max(recursive(node.left)+1,
                           recursive(node.right)+1)
            return 0
        
        return recursive(root)
    
    # 题目二：平衡二叉树
    def isBalanced(self,root):
        '''
        :type root:BinaryTreeNode
        :rtype:bool
        '''
        def recursive(node):
            if node:
                leftDepth = recursive(node.left)
                rightDepth = recursive(node.right)
                if leftDepth or rightDepth:
                    return False
                elif abs(leftDepth - rightDepth) <= 1:
                    return max(leftDepth,rightDepth)+1
                else:
                    return False
            return 0
        
        result = recursive(root)
        if result:
            return True
        else:
            return False