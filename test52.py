class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def getFirstCommonNode1(self,head1,head2):
        '''
        :type head1:ListNode
        :type head2:ListNode
        :rtype:ListNode
        '''
        len1 = len2 = 0
        h1,h2 = head1,head2
        while h1:
            len1,h1 = len1+1,h1.next
        while h2:
            len2,h2 = len2+1,h2.next
        h1,h2 = head1,head2
        if len1 > len2:
            for i in range(len1-len2):
                h1 = h1.next
        if len2 > len1:
            for i in range(len2-len1):
                h2 = h2.next
        while h1 and h1 is not h2:
            h1,h2 = h1.next,h2.next
        return h1