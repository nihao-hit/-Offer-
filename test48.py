'''
最长不含重复字符的子字符串
请从字符串中找出最长的不重复的连续子字符串，计算该最长子字符串的长度。
假设字符串中只包含'a'~'z'的字符。
例如：在字符串'arabcacfr'中，最长的不重复的连续子字符串为'acfr'，长度为4。
'''
class test48():
    def getLongestSubstringWithoutDuplication(self,str):
        if str is None or len(str) == 0:
            return 0
        length = [0]*len(str)
        for i in range(len(str)):
            if i == 0:
                length[i] = 1
            else:
                dupIndex = str[i-length[i-1]:i].rfind(str[i])
                if dupIndex != -1:
                    length[i] = length[i-1]-dupIndex
                else:
                    length[i] = length[i - 1] + 1
        return length[-1]

t = test48()
strS = ['arbcacfr','a','abcde','aaaaaa','']
for str in strS:
    maxLength = t.getLongestSubstringWithoutDuplication(str)
    print(maxLength)
