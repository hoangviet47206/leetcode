class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp = ""
        while (n > 0):
            c = n % 2
            n = n // 2

            tmp = "0" + tmp if (c == 0) else "1" + tmp

        while len(tmp) < 32:
            tmp = "0" + tmp
            
        each = ""
        for i in range(len(tmp) - 1, -1, -1):
            each = each + tmp[i]
        result = 0
        for i in each:
            result = result * 2 + int(i)
        return result
def main():
    sol = Solution()
    result = sol.reverseBits(43261596)
    print(result)
if __name__ == "__main__":
    main()    