'''替换空格'''
class Solution:
    def replaceBlank(self,s):
        '''
        :type s:str
        :rtype:str
        '''
        newS = []
        for i in s:
            if i == ' ':
                newS.append('%20')
            else:
                newS.append(i)
        return ''.join(newS)