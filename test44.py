class Solution:
    def digitAtIndex(self,index):
        '''
        :type index:int
        :rtype:int
        '''
        i = 9
        while index > i:
            index = index-i
            i *= 10
        bits = len(str(i))
        first = i//9-1
        x,y = divmod(index,bits)
        if y == 0:
            return str(first+x)[-1]
        else:
            return str(first+x+1)[y-1]