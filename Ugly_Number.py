class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if(n <= 0): return False
        for i in [2, 3, 5]:
            while (n % i == 0):
                n = n // i
        return n == 1
def main():
    sol = Solution()
    result = sol.isUgly(14)
    print(result)
if __name__ == "__main__":
    main()

        