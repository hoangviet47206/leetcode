# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while (left <= right):
            midle = left + (right - left) // 2
            
            if (isBadVersion(midle)):
                right = midle - 1
            else:
                left = midle + 1
        return left