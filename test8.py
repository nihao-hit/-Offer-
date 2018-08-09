'''二叉树的下一个节点'''
class BinaryTreeNode:
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None
        self.father = None


class Solution:
    def nextNode(self,node):
        '''
        :type node:BinaryTreeNode
        :rtype:BinaryTreeNode
        '''
        if not node:
            return None
        if node.right:
            next = node.right
            while next.left:
                next = next.left
            return next
        if node.father:
            next = node.father
            if next.left == node:
                return next
            while next.father and next.father.left != next:
                next = next.father
            if next.father and next.father.left == next:
                return next.father
'''
以二叉树三节点分析，
如果当前节点为父节点，即有右孩子节点，则中序遍历的下一个节点为右孩子节点的最左节点；
如果当前节点为左孩子节点，即无右孩子节点且当前节点为父节点的左孩子节点，则中序遍历的下一个节点为当前节点的父节点；
如果当前节点为右孩子节点，即无右孩子节点且当前节点为父节点的右孩子节点，则中序遍历的下一个节点为从当前节点的父节点向上遍历找到的第一个以父节点为左孩子节点的父节点。
'''