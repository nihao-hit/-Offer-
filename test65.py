'''
不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用“+”，“-”，“*”，“/”。
'''
class test65():
    def Add(self,num1,num2):
        mySum = num1 ^ num2
        carry = (num1 & num2) << 1
        while carry != 0:
            num1 = mySum
            num2 = carry
            mySum = num1 ^ num2
            carry = (num1 & num2) << 1
        return mySum
t = test65()
print(t.Add(5,6))