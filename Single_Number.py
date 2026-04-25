class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for x in nums:
            i = i ^ x
        return i