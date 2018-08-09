'''从尾到头打印链表'''
class ListNode:
    def __init__(self,v):
        self.val = v
        self.next = None


# 方法1：翻转链表
class Solution1:
    def printReverseValue(self,head):
        '''
        :type head:ListNode
        :rtype:ListNode
        '''
        if not head:
            return head
        if head.next == None:
            print(head.val)
            return head
        if head.next.next == None:
            print('{}\n{}'.format(head.next.val,head.val))
            return head
        prev,mid,tail = head,head.next,head.next.next
        prev.next,mid.next = None,prev
        while tail.next:
            prev,mid,tail.next,tail = mid,tail,mid,tail.next
        tail.next,head = mid,tail
        while tail:
            print(tail.val)
            tail = tail.next
        return head

# 方法2：栈
class Solution2:
    def printReverseValue(self,head):
        '''
        :type head:ListNode
        :rtype:void
        '''
        if not head:
            return None
        stack = []
        while head:
            stack.append(head)
            head = head.next
        for i in range(len(stack)-1,-1,-1):
            print(stack[i].val)

# 方法3：递归栈
class Solution3:
    def printReverseValue(self,head):
        '''
        :type head:ListNode
        :rtype:void
        '''
        def recursion(head):
            if head:
                recursion(head.next)
                print(head.val)
        recursion(head)

            