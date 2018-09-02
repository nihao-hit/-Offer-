class Solution:
    # 快排
    def quickSort(self,nums):
        '''
        :type nums:list[int]
        :rtype:list[int]
        '''
        def findPivot(nums,i,j):
            # 若存在两个数值不同，返回较大者的下标，否则返回-1
            for i in range(i,j):
                if nums[i] != nums[i+1]:
                    return i if nums[i] > nums[i+1] else i+1
            return -1
        def partition(nums,i,j,k):
            # 循环结束时，i=j且nums[i]为第一个大于等于num的值
            num = nums[k]
            while i < j:
                while i < j and nums[i] < num:
                    i += 1
                while i < j and nums[j] >= num:
                    j -= 1
                if i < j:
                    nums[i],nums[j] = nums[j],nums[i]
            return i
        def recursive(nums,i,j):
            k = findPivot(nums,i,j)
            if k == -1:
                return
            index = partition(nums,i,j,k)
            recursive(nums,i,index-1)
            recursive(nums,index,j)
        recursive(nums,0,len(nums)-1)
        return nums

    # 冒泡排序
    def bubbleSort(self,nums):
        '''
        :type nums:list[int]
        :rtype:list[int]
        '''
        n = len(nums)
        for i in range(n-1):
            for j in range(n-1,i,-1):
                if nums[j] < nums[j-1]:
                    nums[j],nums[j-1] = nums[j-1],nums[j]
        return nums

    # 插入排序
    def insertSort(self,nums):
        for i in range(1,len(nums)):
            j = i
            while j >= 1 and nums[j] < nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]
                j -= 1
        return nums
    
    # 选择排序
    def selectSort(self,nums):
        n = len(nums)
        for i in range(n):
            minKey = i
            for j in range(i+1,n):
                if nums[j] < nums[minKey]:
                    minKey = j
            nums[i],nums[minKey] = nums[minKey],nums[i]
        return nums
    
    # 归并排序
    def mergeSort(self,nums):
        def merge(nums,left,mid,right):
            temp = []
            i,j = left,mid
            while i <= mid-1 and j <= right:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid-1:
                temp.append(nums[i])
                i += 1
            while j <= right:
                temp.append(nums[j])
                j += 1
            nums[left:right+1] = temp
        
        n = len(nums)
        k = 1
        while k < n:
            for i in range(0,n,k*2):
                if i+2*k-1 < n:
                    merge(nums,i,i+k,i+k*2-1)
                elif i+k < n:
                    merge(nums,i,i+k,n-1)
            k *= 2
        return nums

    # 堆排序
    def heapSort(self,nums):
        def pushDown(nums,i,j):
            k = i
            while j//2 >= k:
                if 2*k+1 <= j:
                    if nums[k] >= nums[2*k] and nums[k] >= nums[2*k+1]:
                        return
                    elif nums[k] < nums[2*k] and nums[k] < nums[2*k+1]:
                        if nums[2*k] > nums[2*k+1]:
                            nums[k],nums[2*k] = nums[2*k],nums[k]
                            k = 2*k
                        else:
                            nums[k],nums[2*k+1] = nums[2*k+1],nums[k]
                            k = 2*k+1
                    elif nums[k] < nums[2*k]:
                        nums[k],nums[2*k] = nums[2*k],nums[k]
                        k = 2*k
                    else:
                        nums[k],nums[2*k+1] = nums[2*k+1],nums[k]
                        k = 2*k+1
                else:
                    if nums[k] <= nums[2*k]:
                        nums[k],nums[2*k] = nums[2*k],nums[k]
                    return
        
        n = len(nums)
        for i in range((n-1)//2,-1,-1):
            pushDown(nums,i,n-1)
        for i in range(n-1,0,-1):
            nums[0],nums[i] = nums[i],nums[0]
            pushDown(nums,0,i-1)
        return nums

    # 基数排序
    def radixSort(self,nums):
        from collections import deque
        d = {i:deque() for i in range(10)}
        n = len(str(nums[0]))
        length = len(nums)
        for i in range(n-1,-1,-1):
            for num in nums:
                d[num//pow(10,i)].append(num)
            j = 0
            for k in range(10):
                while d[k]:
                    nums[j] = d[k].popleft()
                    j += 1
        return nums

    # 求第k个最小元素
    def selectK(self,nums,k):
        #         o(1)                  if n<=c
        # T(n) <=  
        #         T(n//5)+T(7n/10)+o(n) if n>c
        '''
        :type nums:list[int]
        :type k:int
        :rtype:int
        '''
        def insertSort(nums,left,right):
            for i in range(left+1,right+1):
                j = i
                while j > left and nums[j] < nums[j-1]:
                    nums[j],nums[j-1] = nums[j-1],nums[j]
                    j -= 1
        
        def partition(nums,i,j,num):
            # 返回划分后右边序列的开始，即第一个等于num的数下标，近似为中位数下标
            while i < j:
                while i < j and nums[i] < num:
                    i += 1
                while i < j and nums[j] >= num:
                    j -= 1
                if i < j:
                    nums[i],nums[j] = nums[j],nums[i]
            return i

        def getMiddle(nums,left,right): 
            # 返回中位数值
            n = right-left+1
            if n <= 5:
                insertSort(nums,left,right)
                return nums[left+n//2]
            for i in range((n+1)//5):
                insertSort(nums,left+i*5,left+i*5+4)
                nums[left+i],nums[left+i*5+2] = nums[left+i*5+2],nums[left+i]
            return getMiddle(nums,left,left+(n+1)//5-1)

        def recursive(nums,left,right,k):
            middle = getMiddle(nums,left,right)
            index = partition(nums,left,right,middle)
            if k == index+1:
                return nums[index]
            elif k < index+1:
                return recursive(nums,left,index-1,k)
            else:
                return recursive(nums,index+1,right,k)
        
        return recursive(nums,0,len(nums)-1,k)