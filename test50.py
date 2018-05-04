'''
第一个只出现一次的字符
字符串中第一个只出现一次的字符。
在字符串中找出第一个只出现一次的字符。
如输入'abaccdeff'，输出'b'。
'''
class test50():
    def getFirstNotRepeatingStr(self,str):
        if str is None or len(str) == 0:
            return 0
        values = {}
        for i in str:
            values[i] = 0
        for i in str:
            values[i] += 1
        for k,v in values.items():
            if v == 1:
                return k
        return 0
'''
字符流中第一个只出现一次的字符
例如：当从字符流中只读出前两个字符'go'时，第一个只出现一次的字符是'g'，
当从该字符流中读出'google'时，第一个只出现一次的字符是'l'。
'''
strS = ['',None,'abaccdeff','aaaaaaaa']
t = test50()
for i in strS:
    number = t.getFirstNotRepeatingStr(i)
    print(number)