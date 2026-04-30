class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            re = 0
            while (n > 0):
                re = (re) + ((n % 10)**2)
                n = n // 10
            
            n = re
        return (n == 1)


def main():
    sol = Solution()
    result = sol.isHappy(19)
    print(result)

if __name__ == "__main__":
    main()