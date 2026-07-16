class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = [0] * len(nums)
        first = 0
        last = len(nums) - 1
        for i in nums:
            if i % 2 == 0:
                result[first] = i
                first += 1
            else:
                result[last] = i
                last = last - 1
        
        return result
def main():
    sol = Solution()
    nums = [3, 1, 2, 4]
    result = sol.sortArrayByParity(nums)
    print(result)

if __name__ == "__main__":
    main()
