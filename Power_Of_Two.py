class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n <= 0): return False
        if (n <= 2): return True
        while (n % 2 == 0):
            n = n // 2
        return (n == 1)

def main():
    sol = Solution()

    n = 18
    result = sol.isPowerOfTwo(n)
    print(result)

if __name__ == "__main__":
    main()