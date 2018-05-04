'''
n个骰子的点数
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。
输入n，打印出s的所有可能的值出现的概率。
'''
class test60():
    def PrintProbability(self,number):
        if number < 1:
            return
        maxVal = 6
        probStorage = [[],[]]
        probStorage[0] = [0]*(number*maxVal+1)
        flag = 0
        for i in range(1,maxVal+1):
            probStorage[flag][i] = 1
        for time in range(2,number+1):
            probStorage[1-flag] = [0]*(maxVal*number+1)
            for pCur in range(time,maxVal*time+1):
                diceNum = 1
                while diceNum < pCur and diceNum <= maxVal:
                    probStorage[1-flag][pCur] += probStorage[flag][pCur-diceNum]
                    diceNum += 1
            flag = 1-flag
        total = maxVal**number
        for i in range(number,maxVal*number+1):
            ratio = probStorage[flag][i]/float(total)
            print("{}:{:e}".format(i,ratio))
t = test60()
number = 6
t.PrintProbability(number)