class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return [d[complement], i]
            d[nums[i]] = i


# ===== TEST =====
if __name__ == "__main__":
    sol = Solution()

    print(sol.twoSum([2,7,11,15], 9))      # [0,1]
    print(sol.twoSum([3,2,4], 6))          # [1,2]
    print(sol.twoSum([3,3], 6))            # [0,1]