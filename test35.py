'''复杂链表的复制'''
class ComplexListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.sibling = None


class Solution:
    # 方法一：把原链表节点N与复制后链表节点N'的配对信息<N,N'>放到哈希表中，
    # 以O(N)空间换O(N)时间。
    def clone1(self,head):
        '''
        :type head:ComplexListNode
        :rtype:ComplexListNode
        '''
        if not head:
            return None
        pairInfo = {}
        cHead = ComplexListNode(head.val)
        pairInfo[head] = cHead
        ch,h = cHead,head
        while h.next:
            h = h.next
            ch.next = ComplexListNode(h.val)
            ch = ch.next
            pairInfo[h] = ch
        ch,h = cHead,head
        while h:
            if h.sibling:
               ch.sibling = pairInfo[h.sibling]
            ch,h = ch.next,h.next
        return cHead
    
    # 方法二：第一步：将复制创建的节点链接在原节点的后面；
    #         第二步：复制原节点的sibling指针；
    #           第三步：拆分原链表与复制链表。
    def clone2(self,head):
        if not head:
            return None
        h = head
        while h:
            temp = ComplexListNode(h.val)
            h.next,temp.next,h = temp,h.next,h.next
        h = head
        while h:
            if h.sibling:
                h.next.sibling = h.sibling.next
            h = h.next.next
        ch = cHead = head.next
        h = head
        while h.next.next:
            h.next = h.next.next
            h = h.next
            ch.next = h.next
            ch = ch.next
        return cHead