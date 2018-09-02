class Solution:
    def getCountOfN(self,array,n):
        '''
        :type array:list[int]
        :type n:int
        :rtype:int
        '''
        def getFirstN(array,n):
            i,j = 0,len(array)-1
            while i < j:
                mid = (i+j)//2
                if array[mid] == n:
                    if mid-1 < 0 or array[mid-1] != n:
                        return mid
                    else:
                        j = mid-1
                elif array[mid] > n:
                    j = mid-1
                else:
                    i = mid+1
            return i if array[i] == n else -1

        def getLastN(array,n):
            i,j = 0,len(array)-1
            while i < j:
                mid = (i+j)//2
                if array[mid] == n:
                    if mid+1 >= len(array) or array[mid+1] != n:
                        return mid
                    else:
                        i = mid+1
                elif array[mid] > n:
                    j = mid-1
                else:
                    i = mid+1
            return i if array[i] == n else -1
        
        if array is None or len(array) == 0:
            return 0
        firstIdx = getFirstN(array,n)
        lastIdx = getLastN(array,n)
        if firstIdx == -1 or lastIdx == -1:
            return 0
        return lastIdx-firstIdx+1

    # 题目2：0-(n-1)中缺失的数字
    def getLostNumber(self,array):
        if array is None or len(array) == 0:
            return -1
        i,j = 0,len(array)-1
        while i < j:
            mid = (i+j)//2
            if array[mid] == mid:
                i = mid+1
            else:
                j = mid
        return i if array[i] > i else -1
    
    # 题目3：数组中数值和下标相等的元素
    def getNumSameAsIdx(self,nums):
        '''
        :type nums:list[int]
        :rtype:int
        '''
        if nums is None and len(nums) == 0:
            return []
        def recursive(nums,i,j,result):
            if i > j or nums[i] > i or nums[j] < j:
                return
            if i == j:
                if nums[i] == i:
                    result.append(i)
                return
            mid = (i+j)//2
            if nums[mid] == mid:
                result.append(mid)
                recursive(nums,i,mid-1,result)
                recursive(nums,mid+1,j,result)
            elif nums[mid] < mid:
                recursive(nums,mid+1,j,result)
            else:
                recursive(nums,i,mid-1,result)
        
        result = []
        recursive(nums,0,len(nums)-1,result)
        return result