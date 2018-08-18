'''合并两个排序的链表'''
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution:
    # 实现1：返回新链表
    def combineTwoList1(self,head1,head2):
        '''
        :type head1:ListNode
        :type head2:ListNode
        :rtype:ListNode
        '''
        h = head3 = ListNode(None)
        head1,head2 = head1.next,head2.next
        while head1 and head2:
            if head1.val < head2.val:
                h.next,head1 = ListNode(head1.val),head1.next
            else:
                h.next,head2 = ListNode(head2.val),head2.next
            h = h.next
        while head1:
            h.next,head1 = ListNode(head1.val),head1.next
            h = h.next
        while head2:
            h.next,head2 = ListNode(head2.val),head2.next
            h = h.next
        return head3
    
    # 实现2：返回重组后的新链表
    def combineTwoList2(self,head1,head2):
        h = head = head1
        head1,head2 = head1.next,head2.next
        while head1 and head2:
            if head1.val < head2.val:
                h.next,head1 = head1,head1.next
            else:
                h.next,head2 = head2,head2.next
            h = h.next
        if head1:
            h.next = head1
        else:
            h.next = head2
        return head