class Solution:
    # 问题一：硬币问题：假设有1，3，5三种硬币，数量足够，请问凑足num所需的最小硬币数是多少？
    def minNumberOfCoin(self,coins,num):
        '''
        :type coins:list[int]
        :type num:int
        :rtype:int
        '''
        result = [0]*(num+1)
        for i in coins:
            result[i] = 1
        for i in range(1,num+1):
            result[i] = min([result[i-coin]+1 for coin in coins
                                              if i-coin > 0])
        return result[num]
    
    # 问题二：装配线调度：一个找出通过工厂装配线的最快方式的制造问题。共有两条装配线，
    # 每条有n个装配站；装配线i的第j个装配站表示为Sij，在该站的装配时间是aij，一个汽车底盘进入工厂，
    # 然后进入装配线i（i为1或2），花费时间ei。在通过一条线的第j个装配站后，
    # 这个底盘来到任一条线的第（j+1）个装配站。如果他留在相同的装配线，则没有移动的开销；
    # 但是，如果在装配站Sij后，它移动到了另一条线上，则花费时间tij。
    # 在离开一条线的第n个装配站后，完成的汽车花费时间xi离开工厂。
    # 待求解的问题是确定应该在装配线1内选择哪些站，在装配线2内选择哪些站，才能使汽车通过工厂的总时间最小。
    def assemblyLine(self,linesTime,outTime):
        '''
        :type linesTime:list[tuple(int)]
        :type outTime:list[int]
        :rtype:list[int]
        '''
        n = len(linesTime[0])
        time,symbol = [[[0]*n for i in range(2)] for j in range(2)]
        time[0][0] = sum(linesTime[0][0])
        time[1][0] = sum(linesTime[1][0])
        symbol[0][0],symbol[1][0] = 0,1
        for i in range(1,n):
            for j in range(2):
                x,y = time[j][i-1]+linesTime[j][i][0],time[1-j][i-1]+sum(linesTime[j][i])
                if x < y:
                    time[j][i],symbol[j][i] = x,j
                else:
                    time[j][i],symbol[j][i] = y,1-j
        
        result = []
        if time[0][-1]+outTime[0] < time[1][-1]+outTime[1]:
            line = 0
        else:
            line = 1
        result.append((line+1,n))
        for j in range(n-1,0,-1):
            line = symbol[line][j]
            result.append((line+1,j))
        return list(reversed(result))
    
    # 问题三：字符串相似距离/编辑距离：对于序列S和T，他们之间距离定义为：
    # 对二者其一进行几次一下的操作（1）删去一个字符，（2）插入一个字符，
    # （3）改变一个字符。每进行一次操作，计数增加一。
    # 将S和T变为同一个字符串的最小计数即为她们的距离。给出相应算法 。
    def editDistance(self,string1,string2):
        '''
        :type string1:str
        :type string2:str
        :rtype:int
        '''
        len1,len2 = len(string1),len(string2)
        result = [[0]*(len2+1) for i in range(len1+1)]
        for i in range(len1+1):
            result[i][0] = i
        for j in range(len2+1):
            result[0][j] = j
        for j in range(1,len2+1):
            for i in range(1,len1+1):
                if string1[i-1] == string2[j-1]:
                    flag = 0
                else:
                    flag = 1
                result[i][j] = min(result[i-1][j-1]+flag,result[i-1][j]+1,result[i][j-1]+1)
        return result[-1][-1]
    
    # 问题四：最长递增子序列
    def longestIncreasingSubsequence1(self,nums):
        '''
        :type nums:list[int]
        :rtype:int
        '''
        result = [0]*len(nums)
        result[0],maxLen = 1,0
        for i in range(1,len(nums)):
            temp = j = 0
            while j < i:
                if nums[j] < nums[i] and result[j]+1 > temp:
                    temp = result[j]+1
                j += 1
            result[i] = temp
            maxLen = max(result[i],maxLen)
        return maxLen
    
    # 方法2：记录子序列长度为i时的最小末尾元素，时间复杂度优化为O(nlogn)
    def longestIncreasingSubsequence2(self,nums):
        from sys import maxsize
        n = len(nums)
        result = [maxsize]*(n+1)
        result[1] = nums[0]
        maxLen = 1
        for i in range(1,n):
            l,r = 1,i+1
            while l < r:
                mid = (l+r)//2
                if result[mid] <= nums[i]:
                    l = mid+1
                else:
                    r = mid
            if result[l] > nums[i]:
                result[l] = nums[i]
            else:
                result[l+1] = nums[i]
        for i in range(n,-1,-1):
            if result[i] != maxsize:
                return i
    
    # 问题五：最大连续子序列的和
    def maxSumOfSubsequence(self,nums):
        '''
        :type nums:list[int]
        :rtype:int
        '''
        curMax = lastMax = 0
        for i in nums:
            curMax = max(curMax+i,i)
            lastMax = max(lastMax,curMax)
        return lastMax
    
    # 问题五扩展：最大连续子序列的积
    def maxMultipleOfSubsequence(self,nums):
        '''
        :type nums:list[int]
        :rtype:int
        '''
        curMax = curMin = lastMax = nums[0]
        for i in range(1,len(nums)):
            curMax,curMin = max(curMax*nums[i],curMin*nums[i],nums[i]), \
                            min(curMax*nums[i],curMin*nums[i],nums[i])
            lastMax = max(curMax,lastMax)
        return lastMax
    
    # 问题六：矩阵链乘法
    def multipleOfMatrix(self,nums):
        '''
        :type nums:list[tuple(int)]
        :rtype:int
        '''
        from sys import maxsize
        n = len(nums)
        result = [[maxsize]*i for i in range(n,0,-1)]
        for i in range(n):
            result[i][0] = 0
        for k in range(1,n+1):
            for i in range(n-k+1):
                j = i+1
                while j <= i+k-1:
                    w = nums[i][0]*nums[j][0]*nums[i+k-1][1]
                    result[i][k-1] = min(result[i][k-1],result[i][j-i-1]+result[j][i+k-1-j]+w)
                    j += 1
        return result[0][-1]
    
    # 问题七：0-1背包问题,使用滚动数组压缩空间复杂度为O(2W)
    def backpackOf0And1(self,v,w,W):
        '''
        :type v:list[int]
        :type w:list[int]
        :type W:int
        :rtype:int
        '''
        n = len(v)
        result = [[0]*(W+1) for i in range(2)]
        flag = 0
        for i in range(W+1):
            if w[n-1] <= i:
                result[0][i] = v[n-1]
            else:
                result[0][i] = 0
        for i in range(n-2,-1,-1):
            flag = 1-flag
            for j in range(W+1):
                if w[i] > j:
                    result[flag][j] = result[1-flag][j]
                else:
                    result[flag][j] = max(result[1-flag][j],result[1-flag][j-w[i]]+v[i])
        return result[flag][-1]

    # 区间动态规划
    # 问题八：石子合并
    def pebbleMerge(self,nums):
        '''
        :type nums:list[int]
        :rtype:tuple(int)
        '''
        from sys import maxsize
        n = len(nums)
        result,w = [[[0]*(n+1) for i in range(n)] for j in range(2)]
        for i in range(n):
            w[i][1] = nums[i]
        for k in range(2,n+1):
            for i in range(n):
                w[i][k] = w[i][1]+w[(i+1)%n][k-1]
                j = i+1
                while j <= i+k-1:
                    result[i][k] = max(result[i][k],
                        result[i][j-i]+result[j%n][i+k-j]+w[i][k])
                    j += 1
        maxCount = 0
        for row in result:
            maxCount = max(maxCount,row[-1])
        return maxCount
    
    # 问题九：乘积最大
    def maxMultiple(self,n,m,string):
        '''
        :type n:int
        :type m:int
        :type string:str
        :rtype:int
        '''
        dp = [[0]*min(i,m+1) for i in range(n,0,-1)]
        for i in range(n):
            dp[i][0] = int(string[i:])
        for k in range(1,m+1):
            for i in range(n-k):
                j = i+1
                while j <= n-k:
                    dp[i][k] = max(dp[i][k],dp[j][k-1]*int(string[i:j]))
                    j += 1
        return dp              