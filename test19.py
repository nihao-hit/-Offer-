'''正则表达式匹配'''
class Solution:
    def re(self,string,pattern):
        '''
        :type string:str
        :type pattern:str
        :trype:bool
        '''
        def match(string,i,lens,pattern,j,lenp):
            if i == lens and j == lenp:
                return True
            elif i == lens or j == lenp:
                return False
            if j+1 == lenp:
                return (string[i] == pattern[j] or pattern[j] == '.') and i+1 == lens
            if pattern[j+1] != '*':
                if string[i] == pattern[j] or pattern[j] == '.':
                    return match(string,i+1,lens,pattern,j+1,lenp)
                else:
                    return False
            else:
                if string[i] != pattern[j] and pattern[j] != '.':
                    return match(string,i,lens,pattern,j+2,lenp)
                else:
                    return match(string,i+1,lens,pattern,j,lenp) or \
                           match(string,i+1,lens,pattern,j+2,lenp) or \
                           match(string,i,lens,pattern,j+2,lenp)
        return match(string,0,len(string),pattern,0,len(pattern))