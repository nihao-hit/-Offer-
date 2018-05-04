'''
滑动窗口的最大值
给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。
例如：给定[2,3,4,2,6,2,5,1]和滑动窗口的大小3，那么一共存在6个滑动窗口，它们的最大值分别是[4,4,6,6,6,5]。
'''
class test59():
    def getMaxOfWindows(self,array,n):
        if array is None or len(array) == 0 or n<=0 or n > len(array):
            return None
        maxList = [0]*len(array)
        maxList[n-1] = max(array[:n])
        for i in range(n,len(array)):
            if maxList[i-1] == array[i-n]:
                if i == len(array)-1:
                    maxList[i] = max(array[i-n+1:])
                else:
                    maxList[i] = max(array[i - n + 1:i + 1])
            else:
                maxList[i] = max([array[i],maxList[i-1]])
        return maxList
    def getMaxOfWindows2(self,array,n):
        if array is None or len(array) == 0 or n<=0 or n > len(array):
            return None
        tmp = []
        deque = []
        for i in range(n):
            while len(tmp) != 0 and array[i] > array[tmp[-1]]:
                tmp.pop()
            tmp.append(i)
        for i in range(n,len(array)):
            deque.append(array[tmp[0]])
            while len(tmp) != 0 and array[i]>=array[tmp[-1]]:
                tmp.pop()
            if len(tmp) != 0 and i-tmp[0]>=n:
                tmp.pop(0)
            tmp.append(i)
        deque.append(array[tmp[0]])
        return deque
t = test59()
arrayS = [[2,3,4,2,6,2,5,1],[2,3,4,2,6,2,5,1],[2,3,4,2,6,2,5,1],[],None]
nS = [3,1,8,3,3]
for i in range(len(arrayS)):
    maxList = t.getMaxOfWindows2(arrayS[i],nS[i])
    print(maxList)