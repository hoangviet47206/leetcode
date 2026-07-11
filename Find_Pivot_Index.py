class Solution(object):
    def pivotIndex(self, nums):
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]

        total = prefix[-1]

        for i in range(len(nums)):
            sumL = prefix[i - 1] if i > 0 else 0
            sumR = total - prefix[i]

            if sumL == sumR:
                return i

        return -1

sol = Solution()
nums = list(map(int, input("Nhập mảng: ").split()))
print(sol.pivotIndex(nums))