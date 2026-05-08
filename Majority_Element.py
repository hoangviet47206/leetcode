class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)
        nums.sort()

        n = nums[l // 2]

        return n
def main():
    sol = Solution()
    nums = [3, 2, 3]
    result = sol.majorityElement(nums)
    print (result)

if __name__ == "__main__":
    main()
