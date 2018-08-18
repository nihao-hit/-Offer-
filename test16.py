'''数值的整数次方'''
class Solution:
    # 考虑了base为0的输入，exponent为负数和0的输入。
    def power1(self,base,exponent):
        '''
        :type base:float
        :type exponent:int
        :rtype:float
        '''
        if abs(base) < 0.000001 and exponent <= 0:
            raise ValueError('0的非正数次方没有意义!')
        result = 1
        for i in range(abs(exponent)):
            result *= base
        return result if exponent >= 0 else 1/result
    
    # 方法2：用递归的方式二分乘方，时间复杂度降为log(n)
    def power2(self,base,exponent):
        if abs(base) < 0.000001 and exponent <= 0:
            raise ValueError('0的非正数次方没有意义！')
        def recursive(base,exponent):
            if exponent == 0:
                return 1.0
            if exponent == 1:
                return base
            result = recursive(base,exponent >> 2)
            return result*result if exponent & 1 == 0 else result*result*base
        return recursive(base,abs(exponent)) if exponent >= 0 \
                else 1/recursive(base,abs(exponent))