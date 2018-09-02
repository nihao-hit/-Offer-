class Solution:
    def inversePairs(self,nums):
        '''
        :type nums:list[int]
        :rtype:int
        '''
        def inverseMerge(nums,left,mid,right):
            temp = []
            i,j = mid-1,right
            count = 0
            while i >= left and j >= mid:
                if nums[i] > nums[j]:
                    count += j-mid+1
                    temp.append(nums[i])
                    i -= 1
                else:
                    temp.append(nums[j])
                    j -= 1
            while i >= left:
                temp.append(nums[i])
                i -= 1
            while j >= mid:
                temp.append(nums[j])
                j -= 1
            nums[left:right+1] = reversed(temp)
            return count 
    
        n = len(nums)
        count = 0
        k = 1
        while k < n:
            for i in range(0,n,k*2):
                if i+2*k-1 < n:
                    count += inverseMerge(nums,i,i+k,i+k*2-1)
                elif i+k < n:
                    count += inverseMerge(nums,i,i+k,n-1)
            k *= 2
        return count