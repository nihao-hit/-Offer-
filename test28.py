'''对称的二叉树'''
class BinaryTreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def symmetry(self,head):
        '''
        :type head:BinaryTreeNode
        :rtype:bool
        '''
        def symmetryOrder(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return symmetryOrder(node1.left,node2.left) and \
                   symmetryOrder(node1.right,node2.right)
        return symmetryOrder(head,head)
'''
如果我们定义一个对称前序遍历，即父节点-》右子节点-》左子节点，
那么如果对称前序遍历的序列与前序遍历父节点-》左子节点-》右子节点的序列相同，
则说明二叉树对称.
'''