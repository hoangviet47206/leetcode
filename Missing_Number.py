class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res    
def main():
    sol = Solution()
    nums = [0, 1, 2, 3, 5, 4, 6, 8]
    result = sol.missingNumber(nums)
    print(result)

if __name__ == "__main__":
    main()    