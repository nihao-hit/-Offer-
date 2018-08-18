'''反转链表'''
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution:
    # 方法1
    def reverseList1(self,head):
        '''
        :type head:ListNode
        :rtype:ListNode
        '''
        first = head.next
        if not first:
            return head
        second = first.next
        if not second:
            return head
        third,first.next,second.next = second.next,None,first
        while third:
            first,second,third = second,third,third.next
            second.next = first
        head.next = second
        return head
    
    # 方法2：递归实现
    def reverseList2(self,head):
        def recursive(prev,node):
            phead = None
            if not node.next:
                phead = node
            else:
                phead = recursive(node,node.next)
            node.next = prev
            return phead
        if not head.next:
            return head
        head.next = recursive(None,head.next)
        return head