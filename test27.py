'''二叉树的镜像'''
class BinaryTreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # 方法1：递归
    def getMirror1(self,head):
        '''
        :type head:BinaryTreeNode
        :rtype:BinaryTreeNode
        '''
        def recursive(node):
            if node:
                node.left,node.right = node.right,node.left
                recursive(node.left)
                recursive(node.right)
        recursive(head)
        return head
    
    # 方法2：循环
    def getMirror2(self,head):
        if not head:
            return None
        result = head
        stack = []
        while stack or head:
            while head:
                head.left,head.right = head.right,head.left
                stack.append(head)
                head = head.left
            if stack:
                head = stack.pop()
            head = head.right
        return result