class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0

        while i < len(nums):
            s = i

            while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                i += 1

            if s == i:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[s]) + "->" + str(nums[i]))

            i += 1

        return res
