'''
反转字符串
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
例如输入字符串“I am a student.”，则输出“student. a am I”.
'''
class test58():

    def reverseStr(self,mStr):
        if len(mStr) == 0:
            return ''
        def reverseWord(start, end):
            while start < end:
                tmp = mStr[start]
                mStr[start] = mStr[end]
                mStr[end] = tmp
                start += 1
                end -= 1
        start,end = 0,0
        while end < len(mStr) and start < len(mStr):
            while end < len(mStr) and mStr[end] != ' ':
                end += 1
            end -= 1
            reverseWord(start,end)
            end = end + 2
            start = end
        return mStr
t = test58()
strS = ['I am a student.','fuck','']
for i in strS:
    reversedStr = t.reverseStr(list(i))
    print(''.join(reversedStr))
'''
左旋转字符串
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部，请定义一个函数实现字符串左旋转操作的功能。
比如：输入字符串'abcdefg'和数字2，该函数将返回'cdefgab'
'''
class test582():
    def LeftSpinStr(self,mStr,n):
        if len(mStr) == 0 or n<0 or n > len(mStr):
            return ''
        def reverseWord(start, end):
            while start < end:
                tmp = mStr[start]
                mStr[start] = mStr[end]
                mStr[end] = tmp
                start += 1
                end -= 1
        if n == 0:
            return mStr
        reverseWord(0,len(mStr)-1)
        reverseWord(0,n-1)
        reverseWord(n,len(mStr)-1)
        return mStr

t = test582()
strS = ['abcdefg','fuck','']
nS = [2,4,0]
for i in range(len(strS)):
    spinedStr = t.LeftSpinStr(list(strS[i]),nS[i])
    print(''.join(spinedStr))