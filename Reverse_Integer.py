class Solution(object):
    def reverse(self, x):
        """
        :type x:int
        :rtype: int
        """
        i = 0
        while x > 0:
            j = x % 10
            i = i * 10 + j
            x = x // 10
        return i