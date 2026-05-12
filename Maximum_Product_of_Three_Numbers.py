class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0] < 0 and nums[1] < 0 :
            if (nums[0] * nums[1]) < (nums[len(nums) - 1] * nums[len(nums) -2]):
                return  (nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3])
            else :
                return nums[0] * nums[1] * nums[len(nums) - 1]
            
        result = nums[-1] * nums[-2] * nums[-3]
        return result

def main():
    sol = Solution()
    nums =[-100,-98,-1,2,3,4]
    result = sol.maximumProduct(nums)
    print(result)
if __name__ == "__main__":
    main()
