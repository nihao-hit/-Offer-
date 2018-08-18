'''链表中倒数第k个节点'''
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution:
    def theLastKNode(self,head,k):
        '''
        :type head:ListNode
        :type k:int
        :rtype:ListNode
        '''
        if k <= 0:
            raise ValueError('k应该大于0.')
        nodeK = phead = head.next
        i = 1
        while nodeK and i < k:
            nodeK,i = nodeK.next,i+1
        if i < k or not nodeK:
            raise ValueError('链表节点数小于k.')
        while nodeK.next:
            phead,nodeK = phead.next,nodeK.next
        return phead
    
    # 求链表的中间节点
    # 方法1：求中间节点的后者
    def theMiddleNode1(self,head):
        '''
        :type head:ListNode
        :rtype:ListNode
        '''
        odd = even = head
        while even:
            odd,even = odd.next,even.next
            if even:
                even = even.next
            else:
                return odd
        return odd
    
    # 方法2：求中间节点的前者
    def theMiddleNode2(self,head):
        '''
        :type head:ListNode
        :rtype:ListNode
        '''
        odd = even = head
        while even.next:
            odd,even = odd.next,even.next
            if even.next:
                even = even.next
            else:
                return odd
        return odd