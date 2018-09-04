class Solution:
    # 方法1：转换为全排列概率问题，递归
    def printProbability1(self,n):
        '''
        :type n:int
        :rtype:void
        '''
        if n < 1:
            return
        result = [0]*(6*n+1)
        def recursive(idx,number,result):
            if idx == 0:
                result[number] += 1
                return
            for i in range(1,7):
                recursive(idx-1,number+i,result)
        
        recursive(n,0,result)
        total = pow(6,n)
        print(sum(result))
        for i in range(n,6*n+1):
            print('{}->{:e}'.format(i,result[i]/total))


    def printProbability2(self,number):
        if number < 1:
            return
        probStorage = [[0]*(number*6+1) for i in range(2)]
        flag = 0
        for i in range(1,6+1):
            probStorage[flag][i] = 1
        for time in range(2,number+1):
            flag = 1-flag
            for pCur in range(time,6*time+1):
                probStorage[flag][pCur] = 0
                diceNum = 1
                while diceNum < pCur and diceNum <= 6:
                    probStorage[flag][pCur] += probStorage[1-flag][pCur-diceNum]
                    diceNum += 1
        total = 6**number
        for i in range(number,6*number+1):
            ratio = probStorage[flag][i]/total
            print('{}->{:e}'.format(i,ratio))