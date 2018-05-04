'''
数字在排序数组中出现的次数
统计一个数字在排序数组中出现的次数。
例如：[1,2,3,3,3,3,4,4,5,6,7,7]中，3出现4次，返回4.
'''
def getFirstN(array,n,start,end):
    if start > end:
        return -1
    index = (start+end)//2
    data = array[index]
    if data == n:
        if index > start and array[index-1] != n or index == start:
            return index
        else:
            end = index-1
    elif data < n:
        start = index+1
    else:
        end = index-1
    return getFirstN(array,n,start,end)


def getLastN(array,n,start,end):
    if start > end:
        return -1
    index = (start+end)//2
    data = array[index]
    if data == n:
        if index < end and array[index+1] != n or index == end:
            return index
        else:
            start = index+1
    elif data < n:
        start = index+1
    else:
        end = index-1
    return getFirstN(array,n,start,end)


def getCountOfN(array,n):
    if array is None or len(array) == 0:
        return -1
    firstIndex = getFirstN(array,n,0,len(array)-1)
    lastIndex = getLastN(array,n,0,len(array)-1)
    if firstIndex == -1 or lastIndex == -1:
        return -1
    return lastIndex-firstIndex+1
arrayS = [[1,2,3,3,3,4,5],[1],[1,1,1,1,1],[],None]
nS = [3,1,0,0,0]
for i in range(len(nS)):
    count = getCountOfN(arrayS[i],nS[i])
    print(count)

'''
0~n-1中缺失的数字
一个长度为n-1的递增排序数组中所有数字都是唯一的，并且每个数字都在范围0-n-1之内。
在范围0-n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
'''
def getLostNumber(array,start,end):
    if array is None or len(array) == 0:
        return -1
    if start > end:
        return -1
    index = start+end
    data = array[index]
    if data == index:
        start = index+1
    else:
        if index == start or index > start and array[index-1] == index-1:
            return index
        else:
            end = index-1
    return getLostNumber(array,start,end)
arrayS = [[0,1,2,3,5,6,7,8,9],[]]
for i in arrayS:
    num = getLostNumber(i,0,len(i)-1)
    print(num)