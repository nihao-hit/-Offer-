'''二叉搜索树与双向链表'''
class BST:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # 方法一：自己写的较复杂的以先序遍历为基础的递归算法。
    # 没有充分利用BST的规律
    def convert1(self,root):
        '''
        :type root:BST
        :rtype:BST
        '''
        def recursive(node,prev):
            if node:
                if not node.left and not node.right:
                    if node.val < prev.val:
                        node.right = prev
                        if node.right.left != node:
                            temp = prev.left
                            while temp.right != node:
                                temp = temp.right
                            node.left = temp
                    else:
                        node.left = prev
                        if node.left.right != node:
                            temp = prev.right
                            while temp.left != node:
                                temp = temp.left
                            node.right = temp
                    return node
                else:
                    result = node
                    if node.val < prev.val:
                        while result.right:
                            result = result.right
                        node.left = recursive(node.left,node)
                        node.right = recursive(node.right,prev)
                    else:
                        while result.left:
                            result = result.left
                        node.left = recursive(node.left,prev)
                        node.right = recursive(node.right,node)
                    return result
        return recursive(root,root)
    
    # 方法二：以中序遍历为基础的递归算法。
    # 充分利用了BST的规律：中序遍历序列即排序序列。
    def convert2(self,root):
        lastNode = [None]
        def recursive(node,lastNode):
            if node:
                recursive(node.left,lastNode)
                node.left = lastNode[0]
                if lastNode[0]:
                    lastNode[0].right = node
                lastNode[0] = node
                recursive(node.right,lastNode)
        recursive(root,lastNode)
        while lastNode[0] and lastNode[0].left:
            lastNode[0] = lastNode[0].left
        return lastNode[0]