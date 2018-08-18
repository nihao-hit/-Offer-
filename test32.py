'''从上到下打印二叉树'''
from collections import deque
class BinaryTreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # 题目一：不分行
    def bfs1(self,root):
        '''
        :type root:BinaryTreeNode
        :rtype:void
        '''
        if not root:
            return 
        queue = deque([root])
        while queue:
            root = queue.popleft()
            print(root.val,end=' ')
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        print()

    # 题目二：分行
    def bfs2(self,root):
        if not root:
            return 
        queue = deque([root])
        curNum,nextNum = 1,0
        while queue:
            root = queue.popleft()
            curNum -= 1
            if curNum == 0:
                print(root.val)
            else:
                print(root.val,end=' ')
            if root.left:
                queue.append(root.left)
                nextNum += 1
            if root.right:
                queue.append(root.right)
                nextNum += 1
            if curNum == 0:
                curNum,nextNum = nextNum,0
        print()
    
    # 题目三：之字形打印二叉树
    def bfs3(self,root):
        if not root:
            return
        stack1,stack2 = [root],[]
        while stack1 or stack2:
            if stack1:
                while stack1:
                    root = stack1.pop()
                    print(root.val,end=' ')
                    if root.left:
                        stack2.append(root.left)
                    if root.right:
                        stack2.append(root.right)
            else:
                while stack2:
                    root = stack2.pop()
                    print(root.val,end=' ')
                    if root.right:
                        stack1.append(root.right)
                    if root.left:
                        stack1.append(root.left)
            print()
'''
分行从上到下打印二叉树：需要两个变量分别迭代表示这一层没打印的节点个数和下一层的节点个数。
一个变量做不到记录每层的节点个数。
之字形打印二叉树：既需要队列实现bfs，又需要栈实现每层节点的后进先出，
联想到题目”用两个栈实现队列“，使用两个栈实现算法.
'''