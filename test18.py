'''删除链表的节点'''
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution:
    # 删除链表的节点
    def deleteNode(self,head,node):
        '''
        :type head:ListNode
        :type node:ListNode
        :rtype:ListNode
        '''
        if node.next != None:
            node.val = node.next.val
            node.next = node.next.next
        else:
            phead = head
            while phead.next != node:
                phead = phead.next
            phead.next = node.next
        return head
    
    # 删除链表中重复的节点
    def deleteRepeatNode(self,head):
        '''
        :type head:ListNode
        :rtype:ListNode
        '''
        prev,phead = head,head.next
        if not phead:
            return
        val = phead.val
        while phead.next:
            if phead.next.val != val:
                prev,phead,val = phead,phead.next,phead.next.val
            else:
                prev.next = phead = phead.next.next
                val = phead.val
        return head