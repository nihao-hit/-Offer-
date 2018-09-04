class Solution:
    def add(self,num1,num2):
        '''
        :type num1:int
        :type num2:int
        :rtype:int
        '''
        mySum = num1 ^ num2
        carry = (num1 & num2) << 1
        while carry != 0:
            num1 = mySum
            num2 = carry
            mySum = num1 ^ num2
            carry = (num1 & num2) << 1
        return mySum

    # 题目2：不使用新变量交换两个变量的值
    # 方法1：加减法
    def swap1(self,a,b):
        a = a-b
        b = a+b
        a = b-a
        return a,b
    
    # 方法2：异或
    def swap2(self,a,b):
        a = a^b
        b = a^b
        a = a^b
        return a,b