'''树的子结构'''
class BinaryTreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    

class Solution:
    def hasSubTree(self,head1,head2):
        '''
        :type head1:BinaryTreeNode
        :type head2:BinaryTreeNode
        :rtype:void
        '''
        def handle(node1,node2):
            if not node2:
                return True
            if not node1:
                return False
            if node1.val != node2.val:
                return False
            return handle(node1.left,node2.left) and \
                   handle(node1.right,node2.right)

        def prevOrder(node,head2):
            flag = False
            if node:
                if node.val == head2.val:
                    flag = handle(node,head2)
                if not flag:
                    flag = prevOrder(node.left,head2)
                if not flag:
                    flag = prevOrder(node.right,head2)
            return flag
        
        return prevOrder(head1,head2)
'''
递归易错：如何处理返回条件与递归进行的矛盾性？
    用变量保存递归结果，在函数的最后统一返回变，而不是分别在函数的各处返回不同的结果。
'''