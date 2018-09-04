class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution:
    # 方法1：用数组模拟圆圈，并不弹出元素，而是置为-1；
    # 则搜索下一个弹出元素的时间复杂度大于等于m，小于等于n。
    # 整体时间复杂度为O(N^2)。
    def lastRemaining1(self,array,m):
        '''
        :type array:list[int]
        :type m:int
        :rtype:int
        '''
        def popMthNumber(array,idx,n,m):
            count = 1
            while count < m:
                idx = (idx+1)%n
                if array[idx] != -1:
                    count += 1
            array[idx] = -1
            while array[idx] == -1:
                idx = (idx+1)%n
            return idx

        if array is None or len(array) == 0 or m <= 0:
            return -1
        n = len(array)
        idx = 0
        for i in range(n-1):
            idx = popMthNumber(array,idx,n,m)
        return array[idx]

    # 方法2：用环形链表模拟圆圈，
    # 建链表时间复杂度为0(N)，搜索下一个弹出元素的时间复杂度为O(M)，
    # 整体时间复杂度为O(N*M)。空间复杂度为O(N)
    def lastRemaining2(self,array,m):
        def buildRing(array,n):
            h = head = ListNode(array[0])
            for i in range(1,n):
                h.next = ListNode(array[i])
                h = h.next
            h.next = head
            return head
        
        if array is None or len(array) == 0 or m <= 0:
            return -1
        n = len(array)
        head = buildRing(array,n)
        for i in range(n-1):
            count = 1
            while count < m-1:
                head,count = head.next,count+1
            head.next = head.next.next
            head = head.next
        return head.val