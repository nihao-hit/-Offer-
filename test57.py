class Solution:
    def findNumbersWithSum(self,array,s):
        if array is None or len(array) == 0:
            return None,None
        start = 0
        end = len(array)-1
        while start < end:
            if array[start]+array[end] == s:
                return array[start],array[end]
            elif array[start]+array[end] < s:
                start += 1
            else:
                end -= 1

    # 题目2：和为s的连续正数序列
    def findContinuousSequence(self,s):
        if s is None or s <= 0:
            return []
        result = []
        start,end = 1,2
        he = start + end
        while start <= s//2 and start < end:
            if he == s:
                result.append(list(range(start,end+1)))
                end += 1
                he += end
            elif he < s:
                end += 1
                he += end
            else:
                he -= start
                start += 1
        return result