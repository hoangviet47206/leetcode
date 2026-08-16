class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * 2
        seen = set()
        duup = None
        sum = 0
        for x in nums:
            if x in seen:
                duup = x
            seen.add(x)
            sum += x
        
        sumN = (len(nums) * (len(nums) + 1)) // 2
        tmp = abs(sumN - sum)
        
        result[0] = duup
        if sum > sumN:
            result[1] = duup - tmp
        else:
            result[1] = duup + tmp
        
        return result
def main():
    sol = Solution()
    result = sol.findErrorNums(nums = [2, 2])
    print(result)
if __name__ == "__main__":
    main()
                