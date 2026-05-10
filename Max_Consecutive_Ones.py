class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rev, result = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                result += 1
                if (i == len(nums) - 1):
                 rev = max(rev, result)
            else :
                rev = max(rev, result)
                result = 0
        
        return rev
def main():
    sol = Solution()
    nums = [1,1,0,1,1,1]
    result = sol.findMaxConsecutiveOnes(nums)
    print(result)
if __name__ == "__main__":
    main()

