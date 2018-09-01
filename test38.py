class Solution:
    def permutationOfStr(self,string):
        '''
        :type string:str
        :rtype:void
        '''
        n = len(string)
        flags = [0]*n
        count = [0]
        def recursive(string,n,i,chars,flags,count):
            if i == n:
                print(''.join(chars))
                count[0] += 1
                return
            for j in range(n):
                if flags[j] == 0:
                    flags[j] = 1
                    recursive(string,n,i+1,chars+[string[j]],flags,count)
                    flags[j] = 0
        
        recursive(string,n,0,[],flags,count)
        return count[0]
    
    # 扩展1：字符的所有组合
    def combination(self,string):
        '''
        :type string:str
        :rtype:void
        '''
        def recursive(string,n,length,index,chars):
            if length == 0:
                print(''.join(chars))
                return
            for i in range(index,n):
                recursive(string,n,length-1,i+1,chars+[string[i]])
        
        n = len(string)
        for i in range(1,n+1):
            recursive(string,n,i,0,[])
    
    # 扩展2：八皇后问题
    def eightQueenProblem(self):
        '''
        :type nums:list[int]
        :rtype:list[int]
        '''
        def recursive(path,count,result,flags):
            if count == 8:
                result.append(path)
                return
            for i in range(8):
                if flags[i] == 0:
                    flag = True
                    for j in range(len(path)):
                        if count-j == abs(i-path[j]):
                            flag = False
                            break
                    if flag:
                        flags[i] = 1
                        recursive(path+[i],count+1,result,flags)
                        flags[i] = 0
        
        flags = [0]*8
        result = []
        count = 1
        for i in range(8):
            flags[i] = 1
            recursive([i],count,result,flags)
            flags[i] = 0
        return result