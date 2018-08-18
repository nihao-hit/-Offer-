'''链表中环的入口节点'''
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution:
    def firstNodeOfRing(self,head):
        '''
        :type head:ListNode
        :rtype:ListNode
        '''
        def meetingNode(head):
            if not head.next:
                return None
            l,r = head,head.next
            while r.next and l.val != r.val:
                l,r = l.next,r.next
                if r.next:
                    r = r.next
                else:
                    return None
            if not r.next:
                return None
            return l
        l = r = meetingNode(head)
        if not l:
            return None
        i = 1
        while r.next.val != l.val:
            i,r = i+1,r.next 
        l = r= head.next
        j = 0
        while j < i:
            r,j = r.next,j+1
        while l.val != r.val:
            l,r = l.next,r.next
        return l