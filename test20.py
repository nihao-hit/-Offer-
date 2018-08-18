'''表示数值的字符串'''
import re
class Solution:
    def isNumerial(self,string):
        '''
        :type string:str
        :rtype:bool
        '''
        return re.match(r'((\+|-)?[1-9][0-9]*(\.[0-9]+)?((e|E)(\+|-)?[1-9][0-9]*)?)|(\.[0-9]+)',string).group(0) == string
s = Solution()
result = s.isNumerial('5e2')
print(result)
