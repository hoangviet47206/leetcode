class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        inc = True
        dec = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dec = False
            if nums[i] < nums[i - 1]:
                inc = False

        return inc or dec  
def main():
    sol = Solution()
    nums = [1,2,4,3]
    result = sol.isMonotonic(nums)
    print(result)
if __name__ == "__main__":
    main()
