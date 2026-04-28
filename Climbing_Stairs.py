class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n <= 2): return n

        str = [0] * (n + 1)
        str[1] = 1
        str[2] = 2

        for i in range(3, n + 1):
            str[i] = str[i - 1] + str[i - 2]
        
        return str[n]
    
def main():
    sol = Solution()
    result = sol.climbStairs(5)
    print(result)

if __name__ == "__main__":
    main()