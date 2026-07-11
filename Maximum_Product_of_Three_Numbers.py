class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        product1 = nums[-1] * nums[-2] * nums[-3]

        product2 = nums[0] * nums[1] * nums[-1]

        return max(product1, product2)

def main():
    sol = Solution()
    nums =[-100,-98,-1,2,3,4]
    result = sol.maximumProduct(nums)
    print(result)
if __name__ == "__main__":
    main()
