class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n < 1): return False
        while n % 4 == 0:
            n = n // 4
        return (n == 1)
def main():
    sol = Solution()
    result = sol.isPowerOfFour(8)
    print(result)
if __name__ == "__main__":
    main()
