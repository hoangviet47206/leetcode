class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)  - 1
        while(l <= r):
            mid = l + (r - l) // 2
            if (nums[mid] == target): return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                
                l = mid + 1
        return -1
def main():
    sol = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    result = sol.search(nums, target)
    print(result)
if __name__ == "__main__":
    main()