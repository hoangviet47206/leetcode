class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for i in range(len(nums)):
            s.add(nums[i])


        return (len(nums) != len(s))
def main():
    sol = Solution()
    nums = [1, 2, 4, 1]
    result = sol.containsDuplicate(nums)
    print(result)

if __name__ == "__main__":
    main()